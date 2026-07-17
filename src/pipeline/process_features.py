from feature_extraction.extract_features import (
    extract_features
)

from core.utils import (
    get_videos_by_status,
    update_metadata
)

from core.config import (
    STATUS_OBJECT_DONE,
    STATUS_FEATURE_DONE,
    STATUS_FEATURE_ERROR
)


# ==================================================
# Feature Extraction Pipeline
# ==================================================

def process_features():
    """
    OCR aşaması tamamlanan tüm videolar için
    Feature Extraction işlemini gerçekleştirir.
    """

    videos = get_videos_by_status(
        STATUS_OBJECT_DONE
    )

    total = len(videos)

    print()
    print("=" * 50)
    print("FEATURE EXTRACTION")
    print("=" * 50)
    print()

    print(f"Toplam Video : {total}")
    print()

    for index, (_, video) in enumerate(videos.iterrows(), start=1):

        video_id = video["video_id"]

        print(
            f"[{index}/{total}] {video_id} işleniyor..."
        )

        try:

            extract_features(video_id)

            update_metadata(
                video_id,
                status=STATUS_FEATURE_DONE
            )

            print("   ✓ Tamamlandı")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_FEATURE_ERROR
            )

            print(f"   ✗ Hata : {e}")

    print()
    print("=" * 50)
    print("FEATURE EXTRACTION TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_features()


if __name__ == "__main__":
    main()