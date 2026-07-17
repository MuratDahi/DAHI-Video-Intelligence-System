from pydantic import BaseModel


class VideoResponse(BaseModel):

    video_id: str

    title: str

    thumbnail: str

    duration: float

    ocr: str

    speech: str

    summary: str