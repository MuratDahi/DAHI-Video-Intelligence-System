from core.utils import load_scene_json


# ==================================================
# Private Helpers
# ==================================================

def _get_scene_count(scene_data):
    """
    Videodaki toplam sahne sayısını döndürür.
    """
    return int(scene_data["scene_count"])


# ==================================================
# Public API
# ==================================================

def extract_scene_features(video_id):
    """
    Scene Detection çıktısından Feature üretir.
    """

    scene_data = load_scene_json(video_id)

    features = {

        "scene_count": _get_scene_count(scene_data)

    }

    return features


# ==================================================
# Test
# ==================================================

def main():

    features = extract_scene_features(
        "RLS_000001"
    )

    print(features)


if __name__ == "__main__":
    main()