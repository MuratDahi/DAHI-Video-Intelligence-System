from semantic.speech_encoder import (
    encode_speech
)

from core.utils import (
    get_videos_by_status,
    save_speech_embedding,
    update_metadata
)

from core.config import (
    STATUS_SPEECH_DONE,
    STATUS_SPEECH_EMBEDDING_DONE,
    STATUS_SPEECH_EMBEDDING_ERROR
)


# ==================================================
# Speech Embedding Pipeline
# ==================================================

def process_speech_embeddings():

    videos = get_videos_by_status(
        STATUS_SPEECH_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("SPEECH EMBEDDINGS")
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

            embedding = encode_speech(video_id)

            save_speech_embedding(
                video_id,
                embedding
            )

            update_metadata(
                video_id,
                status=STATUS_SPEECH_EMBEDDING_DONE
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_SPEECH_EMBEDDING_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("SPEECH EMBEDDINGS TAMAMLANDI")
    print("=" * 50)


# ==================================================
# Test
# ==================================================

def main():

    process_speech_embeddings()


if __name__ == "__main__":
    main()