from pathlib import Path
import shutil

from core.config import DATA_FOLDER


# ==================================================
# Klasör Temizle
# ==================================================

def clear_folder(folder: Path):

    if not folder.exists():
        return

    for item in folder.iterdir():

        if item.is_file():

            item.unlink()

        elif item.is_dir():

            shutil.rmtree(item)


# ==================================================
# Data Temizle
# ==================================================

def clean_data():

    print()
    print("=" * 60)
    print("DATA CLEANER")
    print("=" * 60)
    print()

    folders = [

        "features",
        "keyframes",
        "metadata",
        "objects",
        "ocr",
        "scenes",
        "semantic",
        "similarity",
        "speech",
        "vectors"

    ]

    for folder in folders:

        path = DATA_FOLDER / folder

        clear_folder(path)

        print(f"✓ {folder} temizlendi.")

    print()
    print("=" * 60)
    print("TÜM DATA TEMİZLENDİ")
    print("=" * 60)


# ==================================================
# Test
# ==================================================

if __name__ == "__main__":

    clean_data()