import json
from datetime import datetime
from tqdm import tqdm


from scenedetect import open_video, SceneManager
from scenedetect.detectors import ContentDetector

from core.config import (
    SCENES_FOLDER,
    SCENE_THRESHOLD,

    PIPELINE_NAME,
    PIPELINE_VERSION,

    STATUS_METADATA_DONE,
    STATUS_SCENE_DONE,
    STATUS_SCENE_ERROR
)

from core.utils import (
    get_videos_by_status,
    get_video_path,
    update_metadata
)

# ==================================================
# Klasörü oluştur
# ==================================================

SCENES_FOLDER.mkdir(parents=True, exist_ok=True)

# ==================================================
# Sahneleri Tespit Et
# ==================================================

def detect_scenes(video_path):
    """
    Videodaki sahneleri tespit eder.
    """

    video = open_video(str(video_path))

    scene_manager = SceneManager()

    scene_manager.add_detector(
        ContentDetector(
            threshold=SCENE_THRESHOLD
        )
    )

    scene_manager.detect_scenes(video)

    return scene_manager.get_scene_list()

# ==================================================
# JSON Kaydet
# ==================================================

def save_scene_json(video_id, data):

    output_file = SCENES_FOLDER / f"{video_id}.json"

    with open(output_file, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )



# ==================================================
# Tek Videoyu İşle
# ==================================================

def process_video(row):

    video_id = row["video_id"]

    print(f"\nİşleniyor: {video_id}")

    video_path = get_video_path(video_id)

    # Sahneleri bul
    scene_list = detect_scenes(video_path)

    scenes = []

    # Hiç sahne bulunamadıysa tüm videoyu tek sahne kabul et
    if len(scene_list) == 0:

        scenes.append({

            "scene_id": 1,

            "start_frame": 0,
            "end_frame": int(row["frame_count"]) - 1,

            "start_time": 0.0,
            "end_time": float(row["duration"]),

            "duration": float(row["duration"])

        })

    else:

        for index, scene in enumerate(scene_list, start=1):
            start = scene[0]
            end = scene[1]

            start_frame = start.frame_num
            end_frame = end.frame_num - 1

            start_time = round(start.seconds, 2)
            end_time = round(end.seconds, 2)

            scenes.append({

                "scene_id": index,

                "start_frame": start_frame,
                "end_frame": end_frame,

                "start_time": start_time,
                "end_time": end_time,

                "duration": round(end_time - start_time, 2)

            })

    scene_json = {

        "version": PIPELINE_VERSION,

        "pipeline": PIPELINE_NAME,

        "pipeline_stage": "scene_detection",

        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

        "video_id": video_id,

        "total_duration": float(row["duration"]),

        "total_frames": int(row["frame_count"]),

        "scene_count": len(scenes),

        "scenes": scenes

    }

    save_scene_json(video_id, scene_json)

    update_metadata(

        video_id=video_id,

        scene_count=len(scenes),

        status=STATUS_SCENE_DONE

    )

    print(f"{video_id} tamamlandı. ({len(scenes)} sahne)")

# ==================================================
# Ana Program
# ==================================================

def main():

    videos = get_videos_by_status(STATUS_METADATA_DONE)

    if videos.empty:

        print("İşlenecek video bulunamadı.")
        return

    print(f"{len(videos)} video bulundu.\n")

    for _, row in tqdm(
            videos.iterrows(),
            total=len(videos),
            desc="Scene Detection"
    ):

        try:

            process_video(row)

        except Exception as e:

            print(f"\n❌ {row['video_id']} işlenemedi.")

            print(f"Hata: {e}")

            update_metadata(
                video_id=row["video_id"],
                status=STATUS_SCENE_ERROR
            )

    print("\nScene Detection tamamlandı.")


if __name__ == "__main__":
    main()
