import json
from pathlib import Path


VIDEO_METADATA = (
    Path(__file__).resolve().parents[3]
    / "data"
    / "metadata"
    / "video_metadata.json"
)


class VideoService:

    def __init__(self):

        with open(
            VIDEO_METADATA,
            "r",
            encoding="utf-8",
        ) as f:

            self.videos = json.load(f)

    def get_video(
        self,
        video_id: str,
    ):

        for video in self.videos:

            if video["video_id"] == video_id:

                return {

                    "video_id": video["video_id"],

                    "title": video["title"],

                    "thumbnail": video["thumbnail"],

                    "duration": video["duration"],

                    # Şimdilik örnek veriler
                    "ocr": "Henüz OCR analizi yapılmadı.",

                    "speech": "Henüz konuşma analizi yapılmadı.",

                    "summary": "Henüz AI özeti oluşturulmadı."

                }

        return None


video_service = VideoService()