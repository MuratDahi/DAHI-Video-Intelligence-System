import pandas as pd

from src.core.config import METADATA_FILE

# ==================================================
# Metadata Kolonları
# ==================================================

REQUIRED_COLUMNS = [
    "video_id",
    "duration",
    "frame_count",
    "scene_count",
    "keyframe_count",
    "object_count",
    "text_count",
    "status"
]


# ==================================================
# Metadata Migration
# ==================================================

def migrate_metadata():

    print("Metadata okunuyor...")

    df = pd.read_csv(METADATA_FILE)

    added_columns = []

    for column in REQUIRED_COLUMNS:

        if column not in df.columns:

            if column in [
                "scene_count",
                "keyframe_count",
                "object_count",
                "text_count"
            ]:

                df[column] = 0

            else:

                df[column] = ""

            added_columns.append(column)

    # Kolon sırasını düzelt
    df = df[REQUIRED_COLUMNS]

    df.to_csv(
        METADATA_FILE,
        index=False
    )

    print()

    if added_columns:

        print("Eklenen kolonlar:")

        for column in added_columns:
            print(f"  ✓ {column}")

    else:

        print("Metadata zaten güncel.")

    print("\nMigration tamamlandı.")


# ==================================================
# Main
# ==================================================

if __name__ == "__main__":

    migrate_metadata()
