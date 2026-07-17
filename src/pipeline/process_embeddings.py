from embedding.feature_vector import (
    build_feature_vector
)

from embedding.normalizer import (
    normalize
)

from core.utils import (
    get_videos_by_status,
    save_embedding
)

from core.config import (
    STATUS_FEATURE_DONE
)


# ==================================================
# Embedding Pipeline
# ==================================================

def process_embeddings():

    videos = get_videos_by_status(
        STATUS_FEATURE_DONE
    )

    total = len(videos)

    print()
    print("=" * 50)
    print("EMBEDDING")
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

            embedding = normalize(
                vector
            )

            save_embedding(
                video_id,
                embedding
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("EMBEDDING TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_embeddings()


if __name__ == "__main__":
    main()