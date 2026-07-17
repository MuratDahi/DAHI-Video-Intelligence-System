import numpy as np

from core.utils import (
    load_vector,
    load_visual_embedding,
    load_speech_embedding,
    load_ocr_embedding
)


# ==================================================
# Semantic Fusion
# ==================================================

def build_semantic_embedding(video_id):
    """
    Tüm embedding'leri birleştirerek
    tek bir Semantic Embedding oluşturur.
    """

    # -----------------------------
    # Feature Embedding
    # -----------------------------

    feature_embedding = load_vector(
        video_id
    )

    # -----------------------------
    # Visual Embedding
    # -----------------------------

    visual_embedding = load_visual_embedding(
        video_id
    )

    # -----------------------------
    # Speech Embedding
    # -----------------------------

    speech_embedding = load_speech_embedding(
        video_id
    )

    # -----------------------------
    # OCR Embedding
    # -----------------------------

    ocr_embedding = load_ocr_embedding(
        video_id
    )

    # -----------------------------
    # Fusion
    # -----------------------------

    semantic_embedding = np.concatenate(

        (

            feature_embedding,

            visual_embedding,

            speech_embedding,

            ocr_embedding

        )

    )

    return semantic_embedding.astype(
        np.float32
    )


# ==================================================
# Test
# ==================================================

def main():

    video_id = "RLS_000001"

    embedding = build_semantic_embedding(
        video_id
    )

    print()

    print("=" * 60)
    print("FINAL SEMANTIC EMBEDDING")
    print("=" * 60)

    print()

    print("Feature :", load_embedding(video_id).shape)

    print("Visual  :", load_visual_embedding(video_id).shape)

    print("Speech  :", load_speech_embedding(video_id).shape)

    print("OCR     :", load_ocr_embedding(video_id).shape)

    print()

    print("Final Shape :", embedding.shape)

    print()

    print(embedding[:20])


if __name__ == "__main__":
    main()