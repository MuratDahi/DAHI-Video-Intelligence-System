from pathlib import Path

from core.config import (
    METADATA_FILE,
    SCENES_FOLDER,
    KEYFRAMES_METADATA_FOLDER,
    OBJECTS_METADATA_FOLDER,
    TEXT_METADATA_FOLDER,
    FEATURES_FOLDER
)

import pandas as pd


# ==================================================
# Yardımcı Fonksiyonlar
# ==================================================

def count_json_files(folder: Path):
    """
    Klasörde bulunan JSON dosyalarının sayısını döndürür.
    """
    if not folder.exists():
        return 0

    return len(list(folder.glob("*.json")))


# ==================================================
# Dataset Validation
# ==================================================

def validate_dataset():

    metadata = pd.read_csv(METADATA_FILE)

    total_videos = len(metadata)

    scene_count = count_json_files(SCENES_FOLDER)

    keyframe_count = count_json_files(
        KEYFRAMES_METADATA_FOLDER
    )

    object_count = count_json_files(
        OBJECTS_METADATA_FOLDER
    )

    text_count = count_json_files(
        TEXT_METADATA_FOLDER
    )

    feature_count = count_json_files(
        FEATURES_FOLDER / "metadata"
    )

    print()

    print("=" * 55)
    print("DAHI DATASET VALIDATION")
    print("=" * 55)

    print(f"Toplam Video       : {total_videos}")
    print(f"Scene JSON         : {scene_count}")
    print(f"Keyframe JSON      : {keyframe_count}")
    print(f"Object JSON        : {object_count}")
    print(f"Text JSON          : {text_count}")
    print(f"Feature JSON       : {feature_count}")

    print("=" * 55)

    if (
        scene_count == total_videos and
        keyframe_count == total_videos and
        object_count == total_videos and
        text_count == total_videos and
        feature_count == total_videos
    ):

        print("✅ DATASET READY")

    else:

        print("❌ DATASET INCOMPLETE")


# ==================================================
# Test
# ==================================================

def main():

    validate_dataset()


if __name__ == "__main__":
    main()