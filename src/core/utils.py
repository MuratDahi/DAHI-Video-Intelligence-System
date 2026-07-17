from pathlib import Path
import json

import pandas as pd

import numpy as np

from core.config import (
    METADATA_FILE,
    VIDEOS_FOLDER,

    SCENES_FOLDER,

    KEYFRAMES_METADATA_FOLDER,

    OBJECTS_METADATA_FOLDER,

    FEATURES_FOLDER,

    VECTORS_FOLDER,

    EMBEDDINGS_FOLDER,

    SIMILARITY_FOLDER,

    VISUAL_EMBEDDINGS_FOLDER,

    TEXT_METADATA_FOLDER,

    FUSION_EMBEDDINGS_FOLDER,

    SEMANTIC_SIMILARITY_FOLDER,

    SPEECH_METADATA_FOLDER,

    SPEECH_EMBEDDINGS_FOLDER,

    OCR_METADATA_FOLDER,

    OCR_EMBEDDINGS_FOLDER,

    SEARCH_EMBEDDINGS_FOLDER
)


# ==================================================
# Metadata
# ==================================================

def load_metadata():
    """
    metadata.csv dosyasını DataFrame olarak okur.
    """
    return pd.read_csv(METADATA_FILE)


def save_metadata(df):
    """
    Metadata DataFrame'ini kaydeder.
    """
    df.to_csv(METADATA_FILE, index=False)


def update_metadata(video_id, **kwargs):
    """
    Metadata içerisindeki istenilen alanları günceller.
    """

    df = load_metadata()

    mask = df["video_id"] == video_id

    if not mask.any():
        raise ValueError(f"{video_id} bulunamadı.")

    for column, value in kwargs.items():

        if column in df.columns:
            df.loc[mask, column] = value

    save_metadata(df)


def get_videos_by_status(status):
    """
    Belirtilen status'a sahip videoları döndürür.
    """

    df = load_metadata()

    return df[df["status"] == status]


def get_video(video_id):
    """
    Tek bir videonun metadata bilgisini döndürür.
    """

    df = load_metadata()

    row = df[df["video_id"] == video_id]

    if row.empty:
        raise ValueError(f"{video_id} bulunamadı.")

    return row.iloc[0]


# ==================================================
# Video
# ==================================================

def get_video_path(video_id):
    """
    Video dosyasının yolunu döndürür.
    """

    return VIDEOS_FOLDER / f"{video_id}.mp4"


# ==================================================
# JSON Helpers
# ==================================================

def ensure_directory(path: Path):
    """
    Klasör yoksa oluşturur.
    """

    path.mkdir(
        parents=True,
        exist_ok=True
    )


def load_json(path: Path):
    """
    JSON dosyasını okur.
    """

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_json(path: Path, data):
    """
    JSON dosyasını kaydeder.
    """

    ensure_directory(path.parent)

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


# ==================================================
# Scene
# ==================================================

def load_scene_json(video_id):
    """
    Scene Detection çıktısını okur.
    """

    path = SCENES_FOLDER / f"{video_id}.json"

    return load_json(path)


# ==================================================
# Keyframe
# ==================================================

def save_keyframe_json(video_id, data):
    """
    Keyframe JSON dosyasını kaydeder.
    """

    path = (
        KEYFRAMES_METADATA_FOLDER
        / f"{video_id}.json"
    )

    save_json(path, data)


def load_keyframe_json(video_id):
    """
    Keyframe JSON dosyasını okur.
    """

    path = (
        KEYFRAMES_METADATA_FOLDER
        / f"{video_id}.json"
    )

    return load_json(path)


# ==================================================
# Object Detection
# ==================================================

def save_object_json(video_id, data):
    """
    Object Detection JSON dosyasını kaydeder.
    """

    path = (
        OBJECTS_METADATA_FOLDER
        / f"{video_id}.json"
    )

    save_json(path, data)


def load_object_json(video_id):
    """
    Object Detection JSON dosyasını okur.
    """

    path = (
        OBJECTS_METADATA_FOLDER
        / f"{video_id}.json"
    )

    return load_json(path)


# ==================================================
# Text Extraction
# ==================================================

def save_text_json(video_id, data):
    """
    OCR/Text Extraction JSON dosyasını kaydeder.
    """

    path = (
        TEXT_METADATA_FOLDER
        / f"{video_id}.json"
    )

    save_json(path, data)


def load_text_json(video_id):
    """
    OCR/Text Extraction JSON dosyasını okur.
    """

    path = (
        TEXT_METADATA_FOLDER
        / f"{video_id}.json"
    )

    return load_json(path)

# ==================================================
# Feature Extraction
# ==================================================

def save_feature_json(video_id, data):
    """
    Feature Extraction sonucunu JSON olarak kaydeder.
    """

    path = (
        FEATURES_FOLDER
        / "metadata"
        / f"{video_id}.json"
    )

    save_json(path, data)


def load_feature_json(video_id):
    """
    Feature JSON dosyasını okur.
    """

    path = (
        FEATURES_FOLDER
        / "metadata"
        / f"{video_id}.json"
    )

    return load_json(path)

# ==================================================
# Feature Vector
# ==================================================

def save_vector(video_id, vector):
    """
    Feature Vector'ı .npy olarak kaydeder.
    """

    VECTORS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        VECTORS_FOLDER
        / f"{video_id}.npy"
    )

    np.save(
        output_path,
        vector
    )


def load_vector(video_id):
    """
    Feature Vector'ı yükler.
    """

    input_path = (
        VECTORS_FOLDER
        / f"{video_id}.npy"
    )

    return np.load(input_path)

# ==================================================
# Embedding
# ==================================================

def save_embedding(video_id, embedding):
    """
    Embedding'i .npy olarak kaydeder.
    """

    EMBEDDINGS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    np.save(
        output_path,
        embedding
    )


def load_embedding(video_id):
    """
    Embedding'i yükler.
    """

    input_path = (
        EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    return np.load(input_path)


# ==================================================
# Similarity
# ==================================================

def save_similarity(video_id, data):
    """
    Similarity sonucunu JSON olarak kaydeder.
    """

    SIMILARITY_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        SIMILARITY_FOLDER /
        f"{video_id}.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_similarity(video_id):
    """
    Similarity sonucunu okur.
    """

    input_path = (
        SIMILARITY_FOLDER /
        f"{video_id}.json"
    )

    with open(
        input_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# ==================================================
# Visual Embedding
# ==================================================

def save_visual_embedding(video_id, embedding):
    """
    CLIP Visual Embedding'i kaydeder.
    """

    VISUAL_EMBEDDINGS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        VISUAL_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    np.save(
        output_path,
        embedding
    )


def load_visual_embedding(video_id):
    """
    CLIP Visual Embedding'i okur.
    """

    input_path = (
        VISUAL_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    return np.load(input_path)

# ==================================================
# Fusion Embedding
# ==================================================

def save_fusion_embedding(video_id, embedding):
    """
    Semantic Fusion Embedding'i kaydeder.
    """

    FUSION_EMBEDDINGS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        FUSION_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    np.save(
        output_path,
        embedding
    )


def load_fusion_embedding(video_id):
    """
    Semantic Fusion Embedding'i yükler.
    """

    input_path = (
        FUSION_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    return np.load(input_path)

# ==================================================
# Semantic Similarity
# ==================================================

def save_semantic_similarity(video_id, data):
    """
    Semantic Similarity sonucunu JSON olarak kaydeder.
    """

    SEMANTIC_SIMILARITY_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        SEMANTIC_SIMILARITY_FOLDER /
        f"{video_id}.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_semantic_similarity(video_id):
    """
    Semantic Similarity sonucunu okur.
    """

    input_path = (
        SEMANTIC_SIMILARITY_FOLDER /
        f"{video_id}.json"
    )

    with open(
        input_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# ==================================================
# Speech JSON
# ==================================================

def save_speech_json(video_id, data):
    """
    Speech çıktısını JSON olarak kaydeder.
    """

    SPEECH_METADATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        SPEECH_METADATA_FOLDER /
        f"{video_id}.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_speech_json(video_id):

    input_path = (
        SPEECH_METADATA_FOLDER /
        f"{video_id}.json"
    )

    with open(
        input_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# ==================================================
# Speech Embedding
# ==================================================

def save_speech_embedding(video_id, embedding):
    """
    Speech Embedding'i kaydeder.
    """

    SPEECH_EMBEDDINGS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        SPEECH_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    np.save(
        output_path,
        embedding
    )


def load_speech_embedding(video_id):
    """
    Speech Embedding'i yükler.
    """

    input_path = (
        SPEECH_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    return np.load(input_path)

# ==================================================
# OCR JSON
# ==================================================

def save_ocr_json(video_id, data):

    OCR_METADATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        OCR_METADATA_FOLDER /
        f"{video_id}.json"
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def load_ocr_json(video_id):

    input_path = (
        OCR_METADATA_FOLDER /
        f"{video_id}.json"
    )

    with open(
        input_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)

# ==================================================
# OCR EMBEDDING
# ==================================================

def save_ocr_embedding(video_id, embedding):
    """
    OCR Embedding'i kaydeder.
    """

    OCR_EMBEDDINGS_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = (
        OCR_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    np.save(
        output_path,
        embedding)


def load_ocr_embedding(video_id):
    """
    OCR Embedding'i yükler.
    """

    input_path = (
        OCR_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    return np.load(input_path)

# ==================================================
# Search Embedding
# ==================================================

def save_search_embedding(
        video_id,
        embedding
):

    output_path = (
        SEARCH_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    np.save(
        output_path,
        embedding
    )


def load_search_embedding(
        video_id
):

    input_path = (
        SEARCH_EMBEDDINGS_FOLDER /
        f"{video_id}.npy"
    )

    return np.load(
        input_path
    )