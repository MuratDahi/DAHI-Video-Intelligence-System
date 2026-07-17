from search.semantic_search import (
    SemanticSearch
)

from search.ranking import (
    rank_results
)


# ==================================================
# Recommendation Engine
# ==================================================

class RecommendationEngine:

    def __init__(self):

        self.search_engine = SemanticSearch()

    def recommend(
            self,
            query,
            top_k=5
    ):

        results = self.search_engine.search(

            query,

            top_k

        )

        return rank_results(
            results
        )


# ==================================================
# TEST
# ==================================================

def main():

    engine = RecommendationEngine()

    results = engine.recommend(

        "fitness yapan adam",

        top_k=5

    )

    print()

    print("=" * 50)
    print("RECOMMENDATIONS")
    print("=" * 50)

    print()

    for item in results:

        print(item)


if __name__ == "__main__":
    main()