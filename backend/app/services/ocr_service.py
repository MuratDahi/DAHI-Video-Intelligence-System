from pathlib import Path

import easyocr


class OCRService:

    def __init__(self):

        self.reader = easyocr.Reader(
            ["en"],
            gpu=False,
        )

    def get_image_path(
            self,
            video_id: str,
    ):

        root_dir = Path(__file__).resolve().parents[3]

        image_path = (

                root_dir
                / "data"
                / "keyframes"
                / "images"
                / video_id
                / "scene_001.jpg"

        )

        return image_path

    def extract_text(
            self,
            video_id: str,
    ):

        image_path = self.get_image_path(
            video_id,
        )

        result = self.reader.readtext(
            str(image_path),
            detail=0,
        )

        return result


ocr_service = OCRService()