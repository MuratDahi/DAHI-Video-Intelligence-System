import json
from pathlib import Path

from core.config import DATA_FOLDER


class MetadataService:

    def __init__(self):

        self.metadata = {}

        metadata_file = (
            Path(DATA_FOLDER)
            / "metadata"
            / "video_metadata.json"
        )

        if metadata_file.exists():

            with open(
                metadata_file,
                "r",
                encoding="utf-8"
            ) as f:

                videos = json.load(f)

                self.metadata = {

                    item["video_id"]: item

                    for item in videos

                }

    def get(self, video_id):

        return self.metadata.get(video_id)


metadata_service = MetadataService()