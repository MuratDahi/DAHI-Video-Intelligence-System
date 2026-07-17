from typing import List

from fastapi import APIRouter

from backend.app.schemas.search import SearchRequest
from backend.app.schemas.response import SearchResult

from backend.app.services.search_service import (
    search_service
)

router = APIRouter()


@router.post(
    "/search",
    response_model=List[SearchResult]
)
def search(request: SearchRequest):
    print("=" * 50)
    print("SEARCH ENDPOINT ÇALIŞTI")
    print("Query :", request.query)
    print("Top K :", request.top_k)
    print("=" * 50)
    results = search_service.search(

        request.query,

        request.top_k

    )

    print()
    print("=" * 50)
    print("SEARCH RESULTS")
    print("=" * 50)

    for item in results:
        print(item)

    print()

    return results