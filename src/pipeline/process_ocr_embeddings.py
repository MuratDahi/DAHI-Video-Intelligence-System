from semantic.ocr_encoder import (
    encode_ocr
)

from core.utils import (
    get_videos_by_status,
    save_ocr_embedding,
    update_metadata
)

from core.config import (
    STATUS_OCR_DONE,
    STATUS_OCR_EMBEDDING_DONE,
    STATUS_OCR_EMBEDDING_ERROR
)


# ==================================================
# OCR EMBEDDING PIPELINE
# ==================================================

def process_ocr_embeddings():

    videos = get_videos_by_status(
        STATUS_OCR_DONE
    )

    total = len(videos)

    print()

    print("=" * 50)
    print("OCR EMBEDDINGS")
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

            embedding = encode_ocr(video_id)

            save_ocr_embedding(
                video_id,
                embedding
            )

            update_metadata(
                video_id,
                status=STATUS_OCR_EMBEDDING_DONE
            )

            print("   ✓ Kaydedildi")

        except Exception as e:

            update_metadata(
                video_id,
                status=STATUS_OCR_EMBEDDING_ERROR
            )

            print(f"   ✗ {e}")

    print()

    print("=" * 50)
    print("OCR EMBEDDINGS TAMAMLANDI")
    print("=" * 50)


# ==================================================
# TEST
# ==================================================

def main():

    process_ocr_embeddings()


if __name__ == "__main__":
    main()