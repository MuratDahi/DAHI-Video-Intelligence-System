from search.faiss_index import (
    FAISSIndex
)

from search.query_encoder import (
    encode_query
)


# ==================================================
# Semantic Search
# ==================================================

class SemanticSearch:

    def __init__(self):

        self.index = FAISSIndex()

        self.index.build()

    def search(
            self,
            query,
            top_k=5
    ):

        embedding = encode_query(
            query
        )

        results = self.index.search(

            embedding,

            top_k

        )

        return results


# ==================================================
# TEST
# ==================================================

def main():

    search = SemanticSearch()

    results = search.search(

        "spor yapan adam",

        top_k=3

    )

    print()

    print("=" * 50)
    print("SEMANTIC SEARCH")
    print("=" * 50)

    print()

    for item in results:

        print(item)


if __name__ == "__main__":
    main()