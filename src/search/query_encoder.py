import numpy as np

from semantic.sentence_encoder import (
    encode_text
)


# ==================================================
# Query Encoder
# ==================================================

def encode_query(query):
    """
    Kullanıcının yazdığı sorguyu
    embedding'e dönüştürür.
    """

    embedding = encode_text(query)

    return embedding.astype(
        np.float32
    )


# ==================================================
# TEST
# ==================================================

def main():

    query = "spor yapan adam"

    embedding = encode_query(
        query
    )

    print()

    print("=" * 50)
    print("QUERY ENCODER")
    print("=" * 50)

    print()

    print("Shape :", embedding.shape)

    print()

    print(embedding[:20])


if __name__ == "__main__":
    main()