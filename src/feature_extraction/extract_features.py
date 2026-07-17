from feature_extraction.video_features import (
    extract_video_features
)

from feature_extraction.scene_features import (
    extract_scene_features
)

from feature_extraction.object_features import (
    extract_object_features
)



from datetime import datetime

from core.config import (
    PIPELINE_NAME,
    PIPELINE_VERSION,
    STATUS_FEATURE_DONE
)

from core.utils import (
    save_feature_json,
    update_metadata
)




# ==================================================
# Feature Extraction
# ==================================================

def extract_features(video_id):
    """
    Bir videoya ait tüm Feature'ları üretir.
    """
    features = {

        "pipeline": PIPELINE_NAME,

        "version": PIPELINE_VERSION,

        "pipeline_stage": "feature_extraction",

        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "video_id": video_id,

        "video_features": extract_video_features(video_id),

        "scene_features": extract_scene_features(video_id),

        "object_features": extract_object_features(video_id),

    }

    save_feature_json(
        video_id,
        features
    )

    update_metadata(

        video_id=video_id,

        status=STATUS_FEATURE_DONE

    )

    return features


# ==================================================
# Test
# ==================================================

def main():

    features = extract_features(
        "RLS_000001"
    )

    print(features)


if __name__ == "__main__":
    main()