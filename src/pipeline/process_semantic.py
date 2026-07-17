from semantic.clip_encoder import (
    encode_video
)

from core.utils import (
    get_videos_by_status,
    save_visual_embedding,
    update_metadata
)

from core.config import (
    STATUS_FEATURE_VECTOR_DONE,
    STATUS_VISUAL_DONE,
    STATUS_VISUAL_ERROR
)


# ==================================================
# Semantic Pipeline
# ==================================================

def process_semantic():

    videos = get_videos_by_status(
        STATUS_FEATURE_VECTOR_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("SEMANTIC EMBEDDING")
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

            embedding = encode_video(video_id)

            save_visual_embedding(
                video_id,
                embedding
            )

            update_metadata(
                video_id,
                status=STATUS_VISUAL_DONE
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_VISUAL_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("SEMANTIC TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_semantic()


if __name__ == "__main__":
    main()