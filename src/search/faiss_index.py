import faiss
import numpy as np

from pathlib import Path

from core.config import (
    SEARCH_EMBEDDINGS_FOLDER
)


# ==================================================
# FAISS INDEX
# ==================================================

class FAISSIndex:

    def __init__(self):

        self.index = None

        self.video_ids = []

    # ------------------------------------------------

    def build(self):

        embeddings = []

        self.video_ids = []

        files = sorted(

            Path(

                SEARCH_EMBEDDINGS_FOLDER

            ).glob("*.npy")
        )

        if len(files) == 0:

            raise RuntimeError(
                "Search embedding bulunamadı."
            )

        for file in files:

            vector = np.load(file)

            embeddings.append(vector)

            self.video_ids.append(
                file.stem
            )

        matrix = np.vstack(
            embeddings
        ).astype(
            np.float32
        )

        dimension = matrix.shape[1]

        self.index = faiss.IndexFlatIP(
            dimension
        )

        faiss.normalize_L2(
            matrix
        )

        self.index.add(
            matrix
        )

        print()

        print("=" * 50)

        print("FAISS INDEX")

        print("=" * 50)

        print()

        print(
            "Video Sayısı :",
            len(self.video_ids)
        )

        print(
            "Dimension :",
            dimension
        )

        print()

    # ------------------------------------------------

    def search(
            self,
            query_embedding,
            top_k=5
    ):

        query = np.array(
            [query_embedding],
            dtype=np.float32
        )

        faiss.normalize_L2(
            query
        )

        scores, ids = self.index.search(
            query,
            top_k
        )

        results = []

        for score, idx in zip(

                scores[0],

                ids[0]

        ):

            if idx == -1:
                continue

            results.append({

                "video_id":
                    self.video_ids[idx],

                "score":
                    float(score)

            })

        return results


# ==================================================
# TEST
# ==================================================

def main():

    index = FAISSIndex()

    index.build()


if __name__ == "__main__":
    main()