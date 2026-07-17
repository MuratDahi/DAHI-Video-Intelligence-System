from semantic.semantic_similarity import (
    find_semantic_similar_videos
)

from core.utils import (
    get_videos_by_status,
    save_similarity,
    update_metadata
)

from core.config import (
    STATUS_FUSION_DONE,
    STATUS_SIMILARITY_DONE,
    STATUS_SIMILARITY_ERROR
)


# ==================================================
# Semantic Similarity Pipeline
# ==================================================

def process_semantic_similarity():
    """
    Tüm videolar için Semantic Similarity hesaplar.
    """

    videos = get_videos_by_status(
        STATUS_FUSION_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("SEMANTIC SIMILARITY")
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

            similarity = find_semantic_similar_videos(video_id)

            save_similarity(
                video_id,
                similarity
            )

            update_metadata(
                video_id,
                status=STATUS_SIMILARITY_DONE
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_SIMILARITY_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("SEMANTIC SIMILARITY TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_semantic_similarity()


if __name__ == "__main__":
    main()