import numpy as np


# ==================================================
# Min-Max Normalization
# ==================================================

def min_max_normalize(vector):
    """
    Feature Vector'ı 0-1 aralığına normalize eder.
    """

    minimum = np.min(vector)

    maximum = np.max(vector)

    if maximum == minimum:

        return vector

    return (
        vector - minimum
    ) / (
        maximum - minimum
    )


# ==================================================
# Normalize
# ==================================================

def normalize(vector):
    """
    Varsayılan normalizasyon.
    """

    return min_max_normalize(vector)


# ==================================================
# Test
# ==================================================

def main():

    vector = np.array(
        [13.13,394,1,1,1,7,7,0.755],
        dtype=np.float32
    )

    normalized = normalize(vector)

    print(normalized)

    print()

    print("Min :", normalized.min())

    print("Max :", normalized.max())


if __name__ == "__main__":
    main()