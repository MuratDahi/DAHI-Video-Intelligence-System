from core.utils import (
    load_similarity
)


def recommend(
        video_id,
        top_k=10
):
    """
    Videoya ait önerileri döndürür.
    """

    results = load_similarity(
        video_id
    )

    return results[:top_k]


def main():

    recommendations = recommend(
        "RLS_000001"
    )

    print()

    print("=" * 50)
    print("RECOMMENDATIONS")
    print("=" * 50)

    print()

    for index, item in enumerate(
            recommendations,
            start=1
    ):

        print(

            f"{index}. "

            f"{item['video_id']} "

            f"({item['similarity']:.4f})"

        )


if __name__ == "__main__":
    main()