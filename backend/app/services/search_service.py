from .engine import engine
from .metadata_service import metadata_service


class SearchService:

    def search(
        self,
        query: str,
        top_k: int = 5
    ):

        results = engine.recommend(
            query=query,
            top_k=top_k
        )

        enriched_results = []

        for item in results:

            metadata = metadata_service.get(
                item["video_id"]
            )

            if metadata:

                enriched_results.append({

                    "video_id": item["video_id"],

                    "score": item["score"],

                    "title": metadata["title"],

                    "thumbnail": metadata["thumbnail"],

                    "duration": metadata["duration"]

                })

            else:

                enriched_results.append(item)

        return enriched_results


search_service = SearchService()