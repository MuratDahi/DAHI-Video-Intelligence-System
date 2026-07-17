import numpy as np

from core.config import (
    FUSION_EMBEDDINGS_FOLDER
)

from core.utils import (
    load_fusion_embedding
)


# ==================================================
# Cosine Similarity
# ==================================================

def cosine_similarity(vector1, vector2):

    dot_product = np.dot(
        vector1,
        vector2
    )

    norm1 = np.linalg.norm(vector1)

    norm2 = np.linalg.norm(vector2)

    if norm1 == 0 or norm2 == 0:

        return 0.0

    return float(
        dot_product /
        (norm1 * norm2)
    )


# ==================================================
# Semantic Similar Videos
# ==================================================

def find_semantic_similar_videos(
        video_id,
        top_k=10
):
    """
    Semantic Embedding kullanarak
    en benzer videoları bulur.
    """

    target_embedding = load_fusion_embedding(
        video_id
    )

    similarities = []

    for file in FUSION_EMBEDDINGS_FOLDER.glob("*.npy"):

        other_video = file.stem

        if other_video == video_id:
            continue

        embedding = load_fusion_embedding(
            other_video
        )

        score = cosine_similarity(
            target_embedding,
            embedding
        )

        similarities.append({

            "video_id": other_video,

            "similarity": round(score, 4)

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

    results = find_semantic_similar_videos(

        "RLS_000001",

        top_k=10

    )

    print()

    print("=" * 50)

    print("SEMANTIC SIMILARITY")

    print("=" * 50)

    print()

    for index, item in enumerate(

            results,

            start=1

    ):

        print(

            f"{index}. "

            f"{item['video_id']} "

            f"({item['similarity']})"

        )


if __name__ == "__main__":
    main()