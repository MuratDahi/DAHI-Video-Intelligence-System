import json
from pathlib import Path
from collections import Counter
import re

ROOT_DIR = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT_DIR / "data"
from .report_engine import (

    get_video_information,

    get_ocr_report,

    get_speech_report,

    get_object_report,

    get_similarity_report,

    get_scene_report,

    get_dominant_object_report,

    get_video_category,

)


# ==================================================
# JSON OKUMA
# ==================================================

def read_json(path):
    if path.exists():
        with open(
                path,
                "r",
                encoding="utf-8"
        ) as file:
            return json.load(file)

    return None


# ==================================================
# WORD COUNT
# ==================================================
def get_word_count(text):
    return len(
        text.split()
    )


# ==================================================
# CHARACTER COUNT
# ==================================================
def get_character_count(text):
    return len(
        text
    )


# ==================================================
# CONFIDENCE SCORE
# ==================================================
def get_average_confidence(results):
    confidences = []

    for result in results:

        for item in result["texts"]:
            confidences.append(
                item["confidence"]
            )

    if len(confidences) == 0:
        return 0.0

    return round(

        sum(confidences)
        /
        len(confidences),

        2

    )


# ==================================================
# TOP WORDS
# ==================================================
def get_top_words(text):
    words = re.findall(

        r"\b[a-zA-ZçğıöşüÇĞİÖŞÜ]+\b",

        text.lower()

    )

    counts = Counter(
        words
    )

    return [

        word

        for word, count

        in counts.most_common(5)

    ]


# ==================================================
# OCR INSIGHT
# ==================================================
def get_ocr_insight(top_words):
    if len(top_words) == 0:
        return (

            "Videoda okunabilir OCR "
            "metni bulunamadı."

        )

    return (

            "Videoda ağırlıklı olarak "

            + ", ".join(top_words)

            +

            " içerikleri "
            "bulunmaktadır."

    )


# ==================================================
# OCR
# ==================================================

def get_ocr(video_id):
    path = (

            DATA_DIR
            / "ocr"
            / "metadata"
            / f"{video_id}.json"

    )

    data = read_json(path)

    if data is None:
        return {}

    texts = []

    for result in data.get("results", []):

        for item in result.get("texts", []):

            text = item["text"].strip()

            if len(text) <= 1:
                continue

            if item["confidence"] < 0.30:
                continue

            texts.append(text)

    text = "\n".join(
        texts
    )
    word_count = get_word_count(
        text
    )
    character_count = get_character_count(
        text
    )
    confidence = get_average_confidence(
        data.get("results", [])
    )
    top_words = get_top_words(
        text
    )
    insight = get_ocr_insight(
        top_words
    )

    return {

        "text":

            text,

        "text_count":

            len(texts),

        "language":

            "Turkish",

        "word_count":

            word_count,

        "character_count":

            character_count,

        "confidence":

            confidence,

        "top_words":

            top_words,

        "insight":

            insight

    }


# ==================================================
# SPEECH
# ==================================================

def get_speech(video_id):
    path = (

            DATA_DIR
            / "speech"
            / "metadata"
            / f"{video_id}.json"

    )

    data = read_json(path)

    if data is None:
        return {}

    return {

        "text": data["text"],

        "segment_count":
            data["segment_count"],

        "language":
            data["language"]

    }


# ==================================================
# OBJECT
# ==================================================

def get_objects(video_id):
    path = (

            DATA_DIR
            / "objects"
            / "metadata"
            / f"{video_id}.json"

    )

    data = read_json(path)

    if data is None:
        return {}

    results = []

    for scene in data["scenes"]:

        for item in scene["objects"]:
            results.append(

                f'{item["class"]} x {item["count"]}'

            )

    return {

        "total_object":
            data["object_count"],

        "scene_count":
            data["scene_count"],

        "result":
            results

    }


# ==================================================
# FEATURES
# ==================================================

def get_features(video_id):
    path = (

            DATA_DIR
            / "features"
            / "metadata"
            / f"{video_id}.json"

    )

    data = read_json(path)

    if data is None:
        return {}

    return {

        "duration":
            data["video_features"]["duration"],

        "frame_count":
            data["video_features"]["frame_count"],

        "scene_count":
            data["scene_features"]["scene_count"],

        "object_count":
            data["object_features"]["total_objects"],

        "dominant_object":
            data["object_features"]["dominant_object"]

    }


# ==================================================
# SCENES
# ==================================================

def get_scenes(video_id):
    path = (

            DATA_DIR
            / "scenes"
            / f"{video_id}.json"

    )

    data = read_json(path)

    if data is None:
        return {}

    return {

        "scene_count":
            data["scene_count"],

        "duration":
            data["total_duration"],

        "frame_count":
            data["total_frames"]

    }


# ==================================================
# SIMILARITY
# ==================================================

def get_similarity(video_id):
    path = (

            DATA_DIR
            / "similarity"
            / f"{video_id}.json"

    )

    data = read_json(path)

    if data is None:
        return []

    return data


# ==================================================
# VIDEO METADATA
# ==================================================

def get_metadata(video_id):
    path = (

            DATA_DIR
            / "metadata"
            / "video_metadata.json"

    )

    data = read_json(path)

    if data is None:
        return {}

    for item in data:

        if item["video_id"] == video_id:
            return item

    return {}


# ==================================================
# ANALYZE
# ==================================================

def analyze(video_id):
    return {

        "video_id":

            video_id,

        "metadata":

            get_metadata(
                video_id
            ),

        "ocr":

            get_ocr(
                video_id
            ),

        "ocr_report":

            get_ocr_report(

                get_ocr(
                    video_id,
                ),

            ),

        "speech":

            get_speech(
                video_id
            ),

        "speech_report":

            get_speech_report(

                get_speech(
                    video_id,
                ),

            ),

        "objects":

            get_objects(
                video_id
            ),

        "object_report":

            get_object_report(

                get_objects(
                    video_id,
                ),

            ),

        "features":

            get_features(
                video_id
            ),

        "video_report":

            get_video_information(

                get_features(
                    video_id,
                ),

            ),

        "scenes":

            get_scenes(
                video_id
            ),

        "scene_report":

            get_scene_report(

                get_scenes(
                    video_id,
                ),

            ),

        "similarity":

            get_similarity(
                video_id
            ),

        "similarity_report":

            get_similarity_report(

                get_similarity(
                    video_id,
                ),

            ),

        "dominant_object_report":

            get_dominant_object_report(

                get_features(
                    video_id,
                ),

            ),

        "video_category":

            get_video_category(

                get_ocr(
                    video_id,
                ),

                get_speech(
                    video_id,
                ),

            ),

        # ----------------------------------
        # GPT
        # ----------------------------------

        "summary":

            get_ai_summary(
                video_id,
            ),

        "emotion":

            get_emotion(
                video_id,
            ),

        "insight":

            get_dahi_insight(
                video_id,
            ),

    }


# ==================================================
# VIDEO CONTEXT
# ==================================================

def get_video_context(video_id):
    context = []

    ocr = get_ocr(video_id)
    speech = get_speech(video_id)
    objects = get_objects(video_id)
    features = get_features(video_id)
    scenes = get_scenes(video_id)
    similarity = get_similarity(video_id)

    if ocr:
        context.append(

            ocr.get(
                "text",
                "",
            )

        )

    if speech:
        context.append(

            speech.get(
                "text",
                "",
            )

        )

    if objects:
        context.extend(

            objects.get(
                "result",
                [],
            )

        )

    if features:
        context.append(

            str(features)

        )

    if scenes:
        context.append(

            str(scenes)

        )

    if similarity:
        context.append(

            str(similarity)

        )

    return " ".join(context)


def get_ai_summary(video_id):
    return (

        "Bu video için "
        "analiz raporu "
        "hazırlanmaktadır."

    )


def get_emotion(video_id):
    return (

        "Duygu analizi "
        "hazırlanıyor."

    )


# ==================================================
# GPT INSIGHT
# ==================================================
def get_dahi_insight(

        video_id,

):
    metadata = get_metadata(

        video_id,

    )

    ocr = get_ocr(

        video_id,

    )

    speech = get_speech(

        video_id,

    )

    objects = get_objects(

        video_id,

    )

    category = get_video_category(

        ocr,

        speech,

    )

    return (

        f"{metadata['title']} "

        "başlıklı video "

        "başarıyla analiz "

        "edilmiştir.\n\n"


        f"Video "

        f"{category} "

        "kategorisinde "

        "değerlendirilmiştir.\n\n"


        "OCR, konuşma ve "

        "görsel analizler "

        "birlikte "

        "değerlendirilmiştir.\n\n"


        f"Videoda "

        f"{objects['total_object']} "

        "adet nesne "

        "tespit edilmiştir.\n\n"


        "Tüm analizler "
        "birlikte "
        "değerlendirildiğinde "
        "video içerisinde "
        "bilgi aktarımı "
        "yapan bir yapı "
        "bulunduğu "
        "görülmektedir."

    )