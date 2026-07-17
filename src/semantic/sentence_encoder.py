import numpy as np

from semantic.models.sentence_model import SentenceModel


sentence_model = SentenceModel()


# ==================================================
# Encode Text
# ==================================================

def encode_text(text):
    """
    Verilen metni embedding'e dönüştürür.
    """

    embedding = sentence_model.model.encode(
        text,
        convert_to_numpy=True
    )

    return embedding.astype(np.float32)


# ==================================================
# Test
# ==================================================

def main():

    text = "Bugün yeni bir telefon tanıtıldı."

    embedding = encode_text(text)

    print()

    print("Shape :", embedding.shape)

    print()

    print(embedding[:20])


if __name__ == "__main__":
    main()