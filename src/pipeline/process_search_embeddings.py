from semantic.search_embedding import (
    build_search_embedding
)

from core.utils import (
    get_videos_by_status,
    save_search_embedding,
    update_metadata
)

from core.config import (
    STATUS_OCR_EMBEDDING_DONE,
    STATUS_SEARCH_EMBEDDING_DONE,
    STATUS_SEARCH_EMBEDDING_ERROR
)


# ==================================================
# Search Embedding Pipeline
# ==================================================

def process_search_embeddings():

    videos = get_videos_by_status(
        STATUS_OCR_EMBEDDING_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("SEARCH EMBEDDINGS")
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

            embedding = build_search_embedding(
                video_id
            )

            save_search_embedding(
                video_id,
                embedding
            )

            update_metadata(
                video_id,
                status=STATUS_SEARCH_EMBEDDING_DONE
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_SEARCH_EMBEDDING_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("SEARCH EMBEDDINGS TAMAMLANDI")
    print("=" * 50)


# ==================================================
# TEST
# ==================================================

def main():

    process_search_embeddings()


if __name__ == "__main__":
    main()