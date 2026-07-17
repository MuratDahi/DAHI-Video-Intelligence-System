from search.recommendation import (
    RecommendationEngine
)


def main():

    engine = RecommendationEngine()

    while True:

        print()

        query = input("Arama : ")

        if query.lower() == "exit":

            break

        results = engine.recommend(

            query,

            top_k=5

        )

        print()

        print("=" * 50)

        for result in results:

            print(

                result["video_id"],

                "->",

                round(result["score"], 4)

            )


if __name__ == "__main__":
    main()