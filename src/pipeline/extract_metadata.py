import csv
import cv2

from core.config import (
    VIDEOS_FOLDER,
    METADATA_FOLDER,
    METADATA_FILE
)


# ==================================================
# Metadata Extraction
# ==================================================

def main():

    # ----------------------------------------------
    # Metadata klasörü
    # ----------------------------------------------

    METADATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    # ----------------------------------------------
    # metadata.csv oluştur
    # ----------------------------------------------

    if not METADATA_FILE.exists():

        with open(
            METADATA_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                "video_id",

                "duration",

                "frame_count",

                "scene_count",

                "keyframe_count",

                "object_count",

                "text_count",

                "status"

            ])

    # ----------------------------------------------
    # Daha önce eklenen videolar
    # ----------------------------------------------

    existing_videos = set()

    with open(
        METADATA_FILE,
        "r",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        for row in reader:

            existing_videos.add(
                row["video_id"]
            )

    # ----------------------------------------------
    # Videoları tara
    # ----------------------------------------------

    videos = sorted(
        VIDEOS_FOLDER.glob("*.mp4")
    )

    with open(
        METADATA_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        for video in videos:

            video_id = video.stem

            if video_id in existing_videos:

                continue

            cap = cv2.VideoCapture(
                str(video)
            )

            if not cap.isOpened():

                print(f"{video.name} açılamadı.")

                continue

            fps = cap.get(
                cv2.CAP_PROP_FPS
            )

            if fps == 0:

                print(f"{video.name} FPS okunamadı.")

                cap.release()

                continue

            frame_count = int(

                cap.get(
                    cv2.CAP_PROP_FRAME_COUNT
                )

            )

            duration = round(
                frame_count / fps,
                2
            )

            cap.release()

            writer.writerow([

                video_id,

                duration,

                frame_count,

                0,

                0,

                0,

                0,

                "metadata_done"

            ])

            print(
                f"{video_id} metadata oluşturuldu."
            )

    print()

    print("Metadata işlemi tamamlandı.")


# ==================================================
# Main
# ==================================================

if __name__ == "__main__":

    main()