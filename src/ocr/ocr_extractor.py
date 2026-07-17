from pathlib import Path
from datetime import datetime
import json

import easyocr

from core.config import (
    PIPELINE_NAME,
    PIPELINE_VERSION,
    OCR_LANGUAGES,
    OCR_GPU,
    KEYFRAMES_IMAGES_FOLDER,
    OCR_METADATA_FOLDER
)

import cv2
import easyocr

# ==================================================
# EasyOCR
# ==================================================

reader = easyocr.Reader(
    OCR_LANGUAGES,
    gpu=OCR_GPU
)


# ==================================================
# OCR (Tek Görsel)
# ==================================================

def extract_text(image_path):

    image = cv2.imread(str(image_path))

    if image is None:
        raise ValueError(f"Resim okunamadı: {image_path}")

    results = reader.readtext(image)

    texts = []

    for _, text, confidence in results:

        texts.append({
            "text": text,
            "confidence": round(float(confidence), 3)
        })

    return texts

# ==================================================
# OCR (Bir Video)
# ==================================================

def extract_ocr(video_id):

    image_folder = (
        KEYFRAMES_IMAGES_FOLDER /
        video_id
    )

    images = sorted(
        image_folder.glob("*.jpg")
    )

    print(image_folder)
    print(images)
    results = []

    for image in images:

        texts = extract_text(image)

        results.append({

            "image": image.name,

            "texts": texts

        })

    output = {

        "pipeline": PIPELINE_NAME,

        "version": PIPELINE_VERSION,

        "pipeline_stage": "ocr",

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "video_id": video_id,

        "image_count": len(images),

        "results": results

    }

    OCR_METADATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_file = (
        OCR_METADATA_FOLDER /
        f"{video_id}.json"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            ensure_ascii=False,
            indent=4
        )

    return output

if __name__ == "__main__":

    result = extract_ocr("RLS_000001")

    print(result)