from fastapi import APIRouter, HTTPException
print("VIDEO API YÜKLENDİ")
from backend.app.schemas.video import VideoResponse
from backend.app.services.video_service import video_service

router = APIRouter()


@router.get("/video-test")
def video_test():
    return {
        "status": "ok"
    }


print("GET VIDEO ENDPOINT TANIMLANDI")
@router.get(
    "/video/{video_id}",
    response_model=VideoResponse,
)
def get_video(video_id: str):

    video = video_service.get_video(video_id)

    if video is None:
        raise HTTPException(
            status_code=404,
            detail="Video bulunamadı.",
        )

    return video

print(router.routes)