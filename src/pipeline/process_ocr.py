from pathlib import Path

from ocr.ocr_extractor import (
    extract_ocr
)

from core.utils import (
    get_videos_by_status,
    update_metadata
)

from core.config import (
    STATUS_SPEECH_EMBEDDING_DONE,
    STATUS_OCR_DONE,
    STATUS_OCR_ERROR
)
import cv2
import easyocr

# ==================================================
# OCR PIPELINE
# ==================================================

def process_ocr():

    videos = get_videos_by_status(
        STATUS_SPEECH_EMBEDDING_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("OCR EXTRACTION")
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

            extract_ocr(video_id)

            update_metadata(
                video_id,
                status=STATUS_OCR_DONE
            )

            print("   ✓ Tamamlandı")


        except Exception as e:

            import traceback

            traceback.print_exc()

            update_metadata(

                video_id,

                status=STATUS_OCR_ERROR

            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("OCR TAMAMLANDI")
    print("=" * 50)


# ==================================================
# TEST
# ==================================================

def main():

    process_ocr()


if __name__ == "__main__":
    main()