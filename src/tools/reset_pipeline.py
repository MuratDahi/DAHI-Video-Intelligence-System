import sys

from src.core.utils import load_metadata, save_metadata

from src.core.config import PIPELINE_STAGES


# ==================================================
# Tek Bir Pipeline Aşamasını Resetle
# ==================================================

def reset_stage(stage_name):

    if stage_name not in PIPELINE_STAGES:

        print(f"Geçersiz aşama: {stage_name}")
        return

    df = load_metadata()

    stage = PIPELINE_STAGES[stage_name]

    current_status = stage["current_status"]
    previous_status = stage["previous_status"]
    count_column = stage["count_column"]

    # Status'u geri al
    df.loc[
        df["status"] == current_status,
        "status"
    ] = previous_status

    # Sayaç sütununu sıfırla
    if count_column in df.columns:
        df[count_column] = 0

    save_metadata(df)

    print(f"✔ {stage_name} başarıyla resetlendi.")


# ==================================================
# Tüm Pipeline'ı Resetle
# ==================================================

def reset_all():

    df = load_metadata()

    # Status
    df["status"] = "metadata_done"

    # Sayaçlar
    count_columns = [
        "scene_count",
        "keyframe_count",
        "object_count",
        "text_count"
    ]

    for column in count_columns:

        if column in df.columns:

            df[column] = 0

    save_metadata(df)

    print("✔ Tüm pipeline başarıyla resetlendi.")


# ==================================================
# Main
# ==================================================

def main():

    if len(sys.argv) != 2:

        print("Kullanım:")
        print("python reset_pipeline.py scene")
        print("python reset_pipeline.py keyframe")
        print("python reset_pipeline.py object")
        print("python reset_pipeline.py ocr")
        print("python reset_pipeline.py all")

        return

    stage = sys.argv[1].lower()

    if stage == "all":

        reset_all()

    else:

        reset_stage(stage)


if __name__ == "__main__":
    main()