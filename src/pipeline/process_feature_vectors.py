from embedding.feature_vector import (
    build_feature_vector
)

from core.utils import (
    get_videos_by_status,
    save_vector,
    update_metadata
)

from core.config import (
    STATUS_FEATURE_DONE,
    STATUS_FEATURE_VECTOR_DONE,
    STATUS_FEATURE_VECTOR_ERROR
)


# ==================================================
# Feature Vector Pipeline
# ==================================================

def process_feature_vectors():

    videos = get_videos_by_status(
        STATUS_FEATURE_DONE
    )

    total = len(videos)

    print()
    print("=" * 50)
    print("FEATURE VECTOR")
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

            vector = build_feature_vector(
                video_id
            )

            save_vector(
                video_id,
                vector
            )

            update_metadata(
                video_id,
                status=STATUS_FEATURE_VECTOR_DONE
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_FEATURE_VECTOR_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("FEATURE VECTOR TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_feature_vectors()


if __name__ == "__main__":
    main()