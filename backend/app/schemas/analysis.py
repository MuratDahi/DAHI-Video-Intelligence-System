from fastapi import APIRouter

from backend.app.services.engine import analyze


router = APIRouter()


@router.get(
    "/analysis/{video_id}"
)
def get_analysis(
        video_id:str,
):

    return analyze(
        video_id,
    )