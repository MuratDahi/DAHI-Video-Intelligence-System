from embedding.similarity_engine import (
    find_similar_videos
)

from core.utils import (
    get_videos_by_status,
    save_similarity
)

from core.config import (
    STATUS_FEATURE_DONE
)


# ==================================================
# Similarity Pipeline
# ==================================================

def process_similarity():

    videos = get_videos_by_status(
        STATUS_FEATURE_DONE
    )

    total = len(videos)

    print()
    print("=" * 50)
    print("SIMILARITY")
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

            results = find_similar_videos(
                video_id,
                top_k=10
            )

            save_similarity(
                video_id,
                results
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("SIMILARITY TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_similarity()


if __name__ == "__main__":
    main()