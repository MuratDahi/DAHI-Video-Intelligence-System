import numpy as np

from core.utils import load_ocr_json
from semantic.sentence_encoder import encode_text


# ==================================================
# OCR Encoder
# ==================================================

def encode_ocr(video_id):

    data = load_ocr_json(video_id)

    texts = []

    for image in data.get("results", []):

        for item in image.get("texts", []):

            text = item.get(
                "text",
                ""
            ).strip()

            if text:

                texts.append(text)

    merged_text = " ".join(texts).strip()

    if not merged_text:

        return np.zeros(
            384,
            dtype=np.float32
        )

    embedding = encode_text(
        merged_text
    )

    return embedding.astype(
        np.float32
    )


# ==================================================
# Test
# ==================================================

def main():

    video_id = "RLS_000001"

    embedding = encode_ocr(
        video_id
    )

    print()

    print("=" * 50)

    print("OCR EMBEDDING")

    print("=" * 50)

    print()

    print("Shape :", embedding.shape)

    print()

    print(embedding[:20])


if __name__ == "__main__":
    main()