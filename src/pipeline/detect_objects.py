from datetime import datetime

from ultralytics import YOLO
from tqdm import tqdm

from core.config import (
    YOLO_MODEL,
    YOLO_CONFIDENCE,
    KEYFRAMES_IMAGES_FOLDER,
    PIPELINE_NAME,
    PIPELINE_VERSION,
    STATUS_KEYFRAME_DONE,
    STATUS_OBJECT_DONE,
    STATUS_OBJECT_ERROR,
)

from core.utils import (
    get_videos_by_status,
    load_keyframe_json,
    save_object_json,
    update_metadata,
)

from core.config import YOLO_DEVICE

# ==================================================
# YOLO Modeli
# ==================================================

model = YOLO(YOLO_MODEL)


# ==================================================
# Tek Görselde Nesne Tespiti
# ==================================================

def detect_objects(image_path):
    """
    Verilen görsel üzerinde YOLO ile nesne tespiti yapar.
    """

    results = model.predict(
        source=image_path,
        conf=YOLO_CONFIDENCE,
        verbose=False,
        device=YOLO_DEVICE
    )

    detected_objects = []

    for result in results:
        for box in result.boxes:

            class_id = int(box.cls[0])

            detected_objects.append({
                "class": model.names[class_id],
                "confidence": round(float(box.conf[0]), 3)
            })

    return detected_objects


# ==================================================
# Nesneleri Özetle
# ==================================================

def summarize_objects(objects):
    """
    Aynı sınıfa ait nesneleri gruplayarak
    adet ve güven skorlarını hesaplar.
    """

    summary = {}

    for obj in objects:

        class_name = obj["class"]
        confidence = obj["confidence"]

        if class_name not in summary:

            summary[class_name] = {
                "class": class_name,
                "count": 0,
                "max_confidence": confidence,
                "confidence_sum": 0
            }

        summary[class_name]["count"] += 1
        summary[class_name]["confidence_sum"] += confidence

        if confidence > summary[class_name]["max_confidence"]:
            summary[class_name]["max_confidence"] = confidence

    output = []

    for item in summary.values():

        item["avg_confidence"] = round(
            item["confidence_sum"] / item["count"],
            3
        )

        del item["confidence_sum"]

        output.append(item)

    return output


# ==================================================
# Tek Videoyu İşle
# ==================================================

def process_video(row):
    """
    Bir videonun tüm keyframe'leri üzerinde
    nesne tespiti gerçekleştirir.
    """

    video_id = row["video_id"]

    print(f"\nİşleniyor: {video_id}")

    keyframe_data = load_keyframe_json(video_id)

    scene_results = []

    total_objects = 0

    for keyframe in keyframe_data["keyframes"]:

        image_path = (
            KEYFRAMES_IMAGES_FOLDER
            / video_id
            / keyframe["image"]
        )

        objects = detect_objects(image_path)

        summary = summarize_objects(objects)

        scene_object_count = sum(
            obj["count"] for obj in summary
        )

        total_objects += scene_object_count

        scene_results.append({

            "scene_id": keyframe["scene_id"],

            "start_frame": keyframe["start_frame"],

            "end_frame": keyframe["end_frame"],

            "frame_number": keyframe["frame_number"],

            "image": keyframe["image"],

            "objects": summary

        })

    object_json = {

        "pipeline": PIPELINE_NAME,

        "version": PIPELINE_VERSION,

        "pipeline_stage": "object_detection",

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "video_id": video_id,

        "scene_count": keyframe_data["scene_count"],

        "processed_keyframes": len(scene_results),

        "object_count": total_objects,

        "scenes": scene_results

    }

    save_object_json(
        video_id,
        object_json
    )

    update_metadata(
        video_id=video_id,
        object_count=total_objects,
        status=STATUS_OBJECT_DONE
    )

    print(f"{video_id} tamamlandı.")


# ==================================================
# Ana Program
# ==================================================

def main():
    """
    Object Detection Pipeline
    """

    videos = get_videos_by_status(
        STATUS_KEYFRAME_DONE
    )

    if videos.empty:

        print("İşlenecek video bulunamadı.")
        return

    print(f"{len(videos)} video bulundu.\n")

    for _, row in tqdm(
        videos.iterrows(),
        total=len(videos),
        desc="Object Detection"
    ):

        try:

            process_video(row)

        except Exception as e:

            print(f"\n❌ {row['video_id']} işlenemedi.")
            print(f"Hata: {e}")

            update_metadata(
                video_id=row["video_id"],
                status=STATUS_OBJECT_ERROR
            )

    print("\nObject Detection tamamlandı.")


if __name__ == "__main__":
    main()