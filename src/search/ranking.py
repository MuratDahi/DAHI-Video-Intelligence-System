from search.metadata import VideoMetadata

metadata = VideoMetadata()


def rank_results(results):

    results = sorted(

        results,

        key=lambda x: x["score"],

        reverse=True

    )

    final_results = []

    for item in results:

        info = metadata.get(item["video_id"])

        if info is None:
            continue

        final_results.append({

            "video_id": item["video_id"],

            "title": info["title"],

            "thumbnail": info["thumbnail"],

            "duration": info["duration"],

            "score": item["score"]

        })

    return final_results