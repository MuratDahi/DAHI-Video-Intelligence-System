from datetime import datetime

import cv2
from tqdm import tqdm

from core.config import (
    KEYFRAMES_IMAGES_FOLDER,
    KEYFRAME_IMAGE_EXTENSION,
    KEYFRAME_SEARCH_RADIUS,

    PIPELINE_NAME,
    PIPELINE_VERSION,

    STATUS_SCENE_DONE,
    STATUS_KEYFRAME_DONE,
    STATUS_KEYFRAME_ERROR
)

from core.utils import (
    get_videos_by_status,
    get_video_path,
    load_scene_json,
    save_keyframe_json,
    update_metadata
)


# ==================================================
# Klasörleri Oluştur
# ==================================================

KEYFRAMES_IMAGES_FOLDER.mkdir(
    parents=True,
    exist_ok=True
)


# ==================================================
# Frame Keskinliğini Hesapla
# ==================================================

def calculate_sharpness(frame):
    """
    Laplacian Variance kullanarak
    frame'in ne kadar net olduğunu hesaplar.
    """

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    return cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()


# ==================================================
# En İyi Frame'i Bul
# ==================================================

def find_best_frame(cap, scene):

    start_frame = scene["start_frame"]
    end_frame = scene["end_frame"]

    middle_frame = (start_frame + end_frame) // 2

    search_start = max(
        start_frame,
        middle_frame - KEYFRAME_SEARCH_RADIUS
    )

    search_end = min(
        end_frame,
        middle_frame + KEYFRAME_SEARCH_RADIUS
    )

    best_frame = None
    best_frame_number = middle_frame
    best_score = -1

    for frame_number in range(search_start, search_end + 1):

        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            frame_number
        )

        success, frame = cap.read()

        if not success:
            continue

        score = calculate_sharpness(frame)

        if score > best_score:

            best_score = score
            best_frame = frame.copy()
            best_frame_number = frame_number

    return (
        best_frame,
        best_frame_number,
        best_score
    )


# ==================================================
# Keyframe Kaydet
# ==================================================

def save_keyframe(video_id, scene_id, frame):

    output_folder = KEYFRAMES_IMAGES_FOLDER / video_id

    output_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    image_name = (
        f"scene_{scene_id:03d}"
        f"{KEYFRAME_IMAGE_EXTENSION}"
    )

    output_path = output_folder / image_name

    cv2.imwrite(
        str(output_path),
        frame
    )

    return image_name


# ==================================================
# Tek Videoyu İşle
# ==================================================

def process_video(row):

    video_id = row["video_id"]

    print(f"\nİşleniyor: {video_id}")

    scene_data = load_scene_json(video_id)

    video_path = get_video_path(video_id)

    cap = cv2.VideoCapture(str(video_path))

    if not cap.isOpened():
        raise RuntimeError("Video açılamadı.")

    keyframes = []

    for scene in scene_data["scenes"]:

        scene_id = scene["scene_id"]

        frame, frame_number, sharpness = find_best_frame(
            cap,
            scene
        )

        if frame is None:
            continue

        image_name = save_keyframe(
            video_id,
            scene_id,
            frame
        )

        keyframes.append({

            "scene_id": scene_id,

            "start_frame": scene["start_frame"],

            "end_frame": scene["end_frame"],

            "frame_number": frame_number,

            "sharpness_score": round(sharpness, 2),

            "image": image_name

        })

    cap.release()

    keyframe_json = {

        "pipeline": PIPELINE_NAME,

        "version": PIPELINE_VERSION,

        "pipeline_stage": "keyframe_extraction",

        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "video_id": video_id,

        "scene_count": scene_data["scene_count"],

        "keyframe_count": len(keyframes),

        "keyframes": keyframes

    }

    save_keyframe_json(
        video_id,
        keyframe_json
    )

    update_metadata(
        video_id=video_id,
        keyframe_count=len(keyframes),
        status=STATUS_KEYFRAME_DONE
    )

    print(f"{video_id} tamamlandı.")


# ==================================================
# Ana Program
# ==================================================

def main():

    videos = get_videos_by_status(
        STATUS_SCENE_DONE
    )

    if videos.empty:

        print("İşlenecek video bulunamadı.")
        return

    print(f"{len(videos)} video bulundu.\n")

    for _, row in tqdm(
        videos.iterrows(),
        total=len(videos),
        desc="Keyframe Extraction"
    ):

        try:

            process_video(row)

        except Exception as e:

            print(f"\n❌ {row['video_id']} işlenemedi.")
            print(f"Hata: {e}")

            update_metadata(
                video_id=row["video_id"],
                status=STATUS_KEYFRAME_ERROR
            )

    print("\nKeyframe Extraction tamamlandı.")


if __name__ == "__main__":
    main()