from semantic.semantic_fusion import (
    build_semantic_embedding
)

from core.utils import (
    get_videos_by_status,
    save_fusion_embedding,
    update_metadata
)

from core.config import (
    STATUS_SEARCH_EMBEDDING_DONE,
    STATUS_FUSION_DONE,
    STATUS_FUSION_ERROR
)


# ==================================================
# Fusion Pipeline
# ==================================================

def process_fusion():
    """
    Tüm videolar için Semantic Fusion Embedding oluşturur.
    """

    videos = get_videos_by_status(
        STATUS_SEARCH_EMBEDDING_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("SEMANTIC FUSION")
    print("=" * 50)

    print()

    print(f"Toplam Video : {total}")

    print()

    for index, (_, video) in enumerate(
        videos.iterrows(),
        start=1
    ):

        video_id = video["video_id"]

        print(f"[{index}/{total}] {video_id}")

        try:

            embedding = build_semantic_embedding(video_id)

            save_fusion_embedding(
                video_id,
                embedding
            )

            update_metadata(
                video_id,
                status=STATUS_FUSION_DONE
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_FUSION_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("FUSION TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_fusion()


if __name__ == "__main__":
    main()