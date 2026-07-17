from pathlib import Path

from speech.speech_extractor import (
    extract_speech
)

from core.utils import (
    get_videos_by_status,
    save_speech_json,
    update_metadata
)

from core.config import (
    VIDEOS_FOLDER,
    STATUS_VISUAL_DONE,
    STATUS_SPEECH_DONE,
    STATUS_SPEECH_ERROR
)


# ==================================================
# Speech Pipeline
# ==================================================

def process_speech():

    videos = get_videos_by_status(
        STATUS_VISUAL_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("SPEECH EXTRACTION")
    print("=" * 50)

    print()

    print(f"Toplam Video : {total}")

    print()

    for index, (_, video) in enumerate(

            videos.iterrows(),

            start=1

    ):

        video_id = video["video_id"]

        print(

            f"[{index}/{total}] {video_id}"

        )

        try:

            video_path = (
                    VIDEOS_FOLDER /
                    f"{video_id}.mp4"
            )

            speech = extract_speech(
                video_path
            )

            save_speech_json(
                video_id,
                speech
            )

            update_metadata(
                video_id,
                status=STATUS_SPEECH_DONE
            )

            print("   ✓ Tamamlandı")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_SPEECH_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("SPEECH TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_speech()


if __name__ == "__main__":
    main()