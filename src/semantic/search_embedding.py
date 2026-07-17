import numpy as np

from core.utils import (

    load_speech_embedding,

    load_ocr_embedding

)


# ==================================================
# Search Embedding
# ==================================================

def build_search_embedding(video_id):

    speech = load_speech_embedding(
        video_id
    )

    ocr = load_ocr_embedding(
        video_id
    )

    embedding = (

        speech + ocr

    ) / 2

    return embedding.astype(
        np.float32
    )


# ==================================================
# Test
# ==================================================

def main():

    video_id = "RLS_000001"

    embedding = build_search_embedding(
        video_id
    )

    print()

    print("=" * 50)

    print("SEARCH EMBEDDING")

    print("=" * 50)

    print()

    print(
        embedding.shape
    )


if __name__ == "__main__":

    main()