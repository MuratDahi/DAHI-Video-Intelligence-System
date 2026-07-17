import numpy as np

from core.utils import (
    load_embedding
)

from core.config import (
    EMBEDDINGS_FOLDER
)


# ==================================================
# Cosine Similarity
# ==================================================

def cosine_similarity(vector1, vector2):
    """
    İki vektör arasındaki Cosine Similarity değerini hesaplar.
    """

    dot_product = np.dot(vector1, vector2)

    norm1 = np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return float(
        dot_product / (norm1 * norm2)
    )


# ==================================================
# Video Similarity
# ==================================================

def calculate_similarity(video_id_1, video_id_2):
    """
    İki videonun benzerliğini hesaplar.
    """

    embedding1 = load_embedding(video_id_1)
    embedding2 = load_embedding(video_id_2)

    return cosine_similarity(
        embedding1,
        embedding2
    )


# ==================================================
# Find Similar Videos
# ==================================================

def find_similar_videos(video_id, top_k=10):
    """
    Verilen videoya en çok benzeyen videoları bulur.
    """

    target_embedding = load_embedding(video_id)

    similarities = []

    for file in EMBEDDINGS_FOLDER.glob("*.npy"):

        other_video = file.stem

        if other_video == video_id:
            continue

        embedding = load_embedding(other_video)

        score = cosine_similarity(
            target_embedding,
            embedding
        )

        similarities.append({

            "video_id": other_video,

            "similarity": score

        })

    similarities.sort(

        key=lambda x: x["similarity"],

        reverse=True

    )

    return similarities[:top_k]


# ==================================================
# Test
# ==================================================

def main():

    results = find_similar_videos(

        "RLS_000001",

        top_k=10

    )

    print()

    print("=" * 50)
    print("TOP 10 SIMILAR VIDEOS")
    print("=" * 50)
    print()

    for index, item in enumerate(results, start=1):

        print(
            f"{index}. "
            f"{item['video_id']}  "
            f"({item['similarity']:.4f})"
        )


if __name__ == "__main__":
    main()