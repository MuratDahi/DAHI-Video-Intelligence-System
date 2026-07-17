from pathlib import Path
from datetime import datetime
import re

import whisper

from core.config import (
    PIPELINE_NAME,
    PIPELINE_VERSION,
    WHISPER_MODEL
)


# ==================================================
# WHISPER MODEL
# ==================================================

model = whisper.load_model(
    WHISPER_MODEL
)


# ==================================================
# CLEAN TRANSCRIPT
# ==================================================

def clean_transcript(result):
    """
    Whisper çıktısını temizler.
    """

    text = result.get(
        "text",
        ""
    ).strip()

    segments = result.get(
        "segments",
        []
    )

    # Çok kısa metinleri alma

    if len(text) < 10:

        return "", []

    # Türkçe karakter dışındakileri temizle

    text = re.sub(

        r"[^a-zA-Z0-9çğıöşüÇĞİÖŞÜ\s.,!?'-]",

        "",

        text

    )

    text = " ".join(
        text.split()
    )

    # Harf oranı

    letter_count = sum(

        c.isalpha()

        for c in text

    )

    ratio = letter_count / max(
        len(text),
        1
    )

    if ratio < 0.60:

        return "", []

    # Segmentleri temizle

    cleaned_segments = []

    for segment in segments:

        segment_text = segment["text"].strip()

        segment_text = re.sub(

            r"[^a-zA-Z0-9çğıöşüÇĞİÖŞÜ\s.,!?'-]",

            "",

            segment_text

        )

        segment_text = " ".join(
            segment_text.split()
        )

        if len(segment_text) < 3:
            continue

        cleaned_segments.append({

            "start": round(
                segment["start"],
                2
            ),

            "end": round(
                segment["end"],
                2
            ),

            "text": segment_text

        })

    return text, cleaned_segments


# ==================================================
# SPEECH EXTRACTION
# ==================================================

def extract_speech(video_path):

    result = model.transcribe(

        str(video_path),

        language="tr",

        task="transcribe",

        fp16=False,

        temperature=0.0

    )

    text, segments = clean_transcript(
        result
    )
    output = {

        "pipeline": PIPELINE_NAME,

        "version": PIPELINE_VERSION,

        "pipeline_stage": "speech_extraction",

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "language": result.get(
            "language",
            "unknown"
        ),

        "text": text,

        "segment_count": len(
            segments
        ),

        "segments": segments

    }

    return output


# ==================================================
# TEST
# ==================================================

def main():
    base_dir = Path(__file__).resolve().parent.parent.parent

    video_path = (
            base_dir
            / "data"
            / "videos"
            / "RLS_000001.mp4"
    )

    if not video_path.exists():
        print()

        print("Video bulunamadı:")

        print(video_path)

        return

    result = extract_speech(
        video_path
    )

    print()

    print("=" * 50)
    print("SPEECH EXTRACTION")
    print("=" * 50)

    print()

    print(
        "Language :",
        result["language"]
    )

    print(
        "Segments :",
        result["segment_count"]
    )

    print()

    if result["text"] == "":

        print(
            "Konuşma algılanmadı veya kalite filtresinden geçemedi."
        )

    else:

        print(result["text"])

        print()

        print("İlk Segmentler:")

        for segment in result["segments"][:5]:
            print(segment)


if __name__ == "__main__":
    main()