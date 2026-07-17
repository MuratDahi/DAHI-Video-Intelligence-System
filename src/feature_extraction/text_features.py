from core.utils import load_ocr_json


# ==================================================
# Helpers
# ==================================================

def _get_total_words(ocr_data):

    total = 0

    for image in ocr_data["results"]:

        for item in image["texts"]:

            total += len(
                item["text"].split()
            )

    return total


def _get_unique_words(ocr_data):

    words = set()

    for image in ocr_data["results"]:

        for item in image["texts"]:

            for word in item["text"].lower().split():

                words.add(word)

    return len(words)


def _get_average_confidence(ocr_data):

    confidences = []

    for image in ocr_data["results"]:

        for item in image["texts"]:

            confidences.append(
                item["confidence"]
            )

    if not confidences:

        return 0.0

    return round(

        sum(confidences) /
        len(confidences),

        3

    )


# ==================================================
# Public API
# ==================================================

def extract_text_features(video_id):

    ocr_data = load_ocr_json(video_id)

    return {

        "total_words":
            _get_total_words(ocr_data),

        "unique_words":
            _get_unique_words(ocr_data),

        "average_confidence":
            _get_average_confidence(ocr_data)

    }


# ==================================================
# Test
# ==================================================

def main():

    print(

        extract_text_features(
            "RLS_000001"
        )

    )


if __name__ == "__main__":
    main()