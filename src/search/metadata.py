import json
from pathlib import Path

VIDEO_METADATA_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "metadata"
    / "video_metadata.json"
)


class VideoMetadata:

    def __init__(self):

        with open(
            VIDEO_METADATA_PATH,
            "r",
            encoding="utf-8"
        ) as f:

            videos = json.load(f)

        self.data = {
            video["video_id"]: video
            for video in videos
        }

    def get(self, video_id):

        return self.data.get(video_id)