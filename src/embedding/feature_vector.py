import numpy as np

from core.utils import (
    load_feature_json
)


# ==================================================
# Video Features
# ==================================================

def _get_video_features(data):
    """
    Video Feature'larını döndürür.
    """

    video = data["video_features"]

    return [

        video["duration"],

        video["frame_count"]

    ]


# ==================================================
# Scene Features
# ==================================================

def _get_scene_features(data):
    """
    Scene Feature'larını döndürür.
    """

    scene = data["scene_features"]

    return [

        scene["scene_count"]

    ]


# ==================================================
# Object Features
# ==================================================

def _get_object_features(data):
    """
    Object Feature'larını döndürür.
    """

    objects = data["object_features"]

    return [

        objects["total_objects"],

        objects["unique_objects"]

    ]



# ==================================================
# Feature Vector Builder
# ==================================================

def build_feature_vector(video_id):
    """
    Feature JSON dosyasını okuyarak
    Feature Vector oluşturur.
    """

    data = load_feature_json(video_id)

    vector = []

    vector.extend(
        _get_video_features(data)
    )

    vector.extend(
        _get_scene_features(data)
    )

    vector.extend(
        _get_object_features(data)
    )



    return np.array(
        vector,
        dtype=np.float32
    )


# ==================================================
# Test
# ==================================================

def main():

    vector = build_feature_vector(
        "RLS_000001"
    )

    print(vector)

    print()

    print("Shape :", vector.shape)

    print("Type  :", vector.dtype)


if __name__ == "__main__":
    main()