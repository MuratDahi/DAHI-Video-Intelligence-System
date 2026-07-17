from pathlib import Path

import numpy as np
import torch
from PIL import Image

from semantic.models.models import ClipModel

from core.utils import (
    save_visual_embedding
)

# ==================================================
# CLIP MODEL
# ==================================================

clip = ClipModel()


# ==================================================
# Encode Single Image
# ==================================================

def encode_image(image_path):
    """
    Tek bir resmi CLIP embedding'ine dönüştürür.
    """

    image = Image.open(image_path).convert("RGB")

    image = clip.preprocess(image).unsqueeze(0)

    image = image.to(clip.device)

    with torch.no_grad():

        embedding = clip.model.encode_image(image)

        embedding /= embedding.norm(
            dim=-1,
            keepdim=True
        )

    return embedding.squeeze().cpu().numpy()


# ==================================================
# Get Keyframes
# ==================================================

def get_keyframes(video_id):
    """
    Videoya ait bütün keyframe'leri döndürür.
    """

    base_dir = Path(__file__).resolve().parent.parent.parent

    keyframe_folder = (
        base_dir
        / "data"
        / "keyframes"
        / "images"
        / video_id
    )

    if not keyframe_folder.exists():

        raise FileNotFoundError(
            f"Keyframe klasörü bulunamadı:\n{keyframe_folder}"
        )

    images = sorted(
        keyframe_folder.glob("*.jpg")
    )

    if len(images) == 0:

        raise FileNotFoundError(
            "Keyframe bulunamadı."
        )

    return images


# ==================================================
# Encode Video
# ==================================================

def encode_video(video_id):
    """
    Videonun bütün keyframe'lerini encode eder.

    Ortalama alınarak tek Visual Embedding üretilir.
    """

    images = get_keyframes(video_id)

    embeddings = []

    print()

    print(f"{video_id}")

    print(f"Toplam Keyframe : {len(images)}")

    for image in images:

        embedding = encode_image(image)

        embeddings.append(
            embedding
        )

    embeddings = np.array(
        embeddings
    )

    visual_embedding = embeddings.mean(
        axis=0
    )

    return visual_embedding


# ==================================================
# Test
# ==================================================

def main():

    video_id = "RLS_000001"

    embedding = encode_video(
        video_id
    )

    save_visual_embedding(
        video_id,
        embedding
    )

    print()

    print("=" * 50)
    print("VISUAL EMBEDDING")
    print("=" * 50)

    print()

    print("Shape :", embedding.shape)

    print()

    print("İlk 20 değer:")

    print(embedding[:20])

    print()

    print("Visual embedding kaydedildi.")


if __name__ == "__main__":
    main()