from pathlib import Path

# Klasörler
BASE_DIR = Path(__file__).resolve().parent.parent

VIDEO_FOLDER = BASE_DIR / "data" / "videos"
METADATA_FOLDER = BASE_DIR / "data" / "metadata"

COUNTER_FILE = METADATA_FOLDER / "video_counter.txt"

# Metadata klasörü yoksa oluştur
METADATA_FOLDER.mkdir(parents=True, exist_ok=True)

# Sayaç dosyası yoksa oluştur
if not COUNTER_FILE.exists():
    COUNTER_FILE.write_text("1")


def get_next_number():
    number = int(COUNTER_FILE.read_text().strip())
    return number


def save_next_number(number):
    COUNTER_FILE.write_text(str(number))


current_number = get_next_number()

# Dosyaları sırala (her çalıştırmada aynı sıra)
videos = sorted(VIDEO_FOLDER.glob("*.mp4"))

for video in videos:

    # Daha önce isimlendirilmişse geç
    if video.stem.startswith("RLS_"):
        continue

    new_name = f"RLS_{current_number:06d}.mp4"

    new_path = VIDEO_FOLDER / new_name

    video.rename(new_path)

    print(f"{video.name}  --->  {new_name}")

    current_number += 1

save_next_number(current_number)

print("\nİşlem tamamlandı.")