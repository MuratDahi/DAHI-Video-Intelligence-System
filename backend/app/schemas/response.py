from pydantic import BaseModel


class SearchResult(BaseModel):

    video_id: str

    title: str

    thumbnail: str

    duration: float

    score: float