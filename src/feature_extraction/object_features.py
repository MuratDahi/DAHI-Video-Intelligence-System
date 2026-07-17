from core.utils import load_object_json


# ==================================================
# Private Helpers
# ==================================================

def _get_total_objects(object_data):
    """
    Videodaki toplam nesne sayısını döndürür.
    """

    return int(object_data["object_count"])


def _get_unique_objects(object_data):
    """
    Farklı nesne sınıfı sayısını döndürür.
    """

    unique_classes = set()

    for scene in object_data["scenes"]:

        for obj in scene["objects"]:

            unique_classes.add(obj["class"])

    return len(unique_classes)


def _get_dominant_object(object_data):
    """
    Videoda en fazla bulunan nesne sınıfını döndürür.
    """

    counts = {}

    for scene in object_data["scenes"]:

        for obj in scene["objects"]:

            class_name = obj["class"]
            count = obj["count"]

            counts[class_name] = counts.get(class_name, 0) + count

    if not counts:
        return None

    return max(
        counts,
        key=counts.get
    )


# ==================================================
# Public API
# ==================================================

def extract_object_features(video_id):
    """
    Object Detection çıktısından Feature üretir.
    """

    object_data = load_object_json(video_id)

    features = {

        "total_objects": _get_total_objects(object_data),

        "unique_objects": _get_unique_objects(object_data),

        "dominant_object": _get_dominant_object(object_data)

    }

    return features


# ==================================================
# Test
# ==================================================

def main():

    features = extract_object_features(
        "RLS_000001"
    )

    print(features)


if __name__ == "__main__":
    main()