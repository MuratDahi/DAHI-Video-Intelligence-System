from core.utils import (
    load_speech_json
)

from semantic.sentence_encoder import (
    encode_text
)


# ==================================================
# Speech Encoder
# ==================================================

def encode_speech(video_id):
    """
    Speech JSON dosyasını okuyup
    tek bir Speech Embedding üretir.
    """

    data = load_speech_json(video_id)

    text = data.get("text", "").strip()

    if len(text) == 0:
        return encode_text("")

    return encode_text(text)


# ==================================================
# Test
# ==================================================

def main():

    video_id = "RLS_000001"

    embedding = encode_speech(video_id)

    print()

    print("=" * 50)
    print("SPEECH EMBEDDING")
    print("=" * 50)

    print()

    print("Shape :", embedding.shape)

    print()

    print(embedding[:20])


if __name__ == "__main__":
    main()