import time

from pipeline.process_features import main as features
from pipeline.process_feature_vectors import main as vectors
from pipeline.process_semantic import main as visual
from pipeline.process_speech import main as speech
from pipeline.process_speech_embeddings import main as speech_embeddings
from pipeline.process_ocr import main as ocr
from pipeline.process_ocr_embeddings import main as ocr_embeddings
from pipeline.process_fusion import main as fusion
from pipeline.process_semantic_similarity import main as similarity
from pipeline.process_search_embeddings import (
    main as search_embeddings
)

def run_step(title, function):

    print()
    print("=" * 70)
    print(title)
    print("=" * 70)

    start = time.time()

    function()

    elapsed = time.time() - start

    print()
    print(f"✓ {title} tamamlandı ({elapsed:.2f} sn)")


def main():

    print()
    print("=" * 70)
    print("DAHI PHASE 2")
    print("=" * 70)

    run_step(
        "Feature Extraction",
        features
    )

    run_step(
        "Feature Embeddings",
        vectors
    )

    run_step(
        "Visual Embeddings",
        visual
    )

    run_step(
        "Speech Extraction",
        speech
    )

    run_step(
        "Speech Embeddings",
        speech_embeddings
    )

    run_step(
        "OCR Extraction",
        ocr
    )

    run_step(
        "OCR Embeddings",
        ocr_embeddings
    )

    run_step(
        "Search Embeddings",
        search_embeddings
    )

    run_step(
        "Semantic Fusion",
        fusion
    )

    run_step(
        "Semantic Similarity",
        similarity
    )

    print()
    print("=" * 70)
    print("PHASE 2 COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()