from core.utils import get_video


# ==================================================
# Video Features
# ==================================================

def _get_duration(video):
    return float(video["duration"])


def _get_frame_count(video):
    return int(video["frame_count"])


# ==================================================
# Feature Extraction
# ==================================================

def extract_video_features(video_id):

    video = get_video(video_id)

    return {
        "duration": _get_duration(video),
        "frame_count": _get_frame_count(video)
    }


# ==================================================
# Test
# ==================================================

def main():

    features = extract_video_features(
        "RLS_000001"
    )

    print(features)


if __name__ == "__main__":
    main()