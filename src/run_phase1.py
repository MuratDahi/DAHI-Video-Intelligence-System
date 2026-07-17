import time

from pipeline.extract_metadata import main as metadata
from pipeline.scene_detection import main as scenes
from pipeline.extract_keyframes import main as keyframes
from pipeline.detect_objects import main as objects


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
    print("DAHI PHASE 1")
    print("=" * 70)

    run_step(
        "Metadata Extraction",
        metadata
    )

    run_step(
        "Scene Detection",
        scenes
    )

    run_step(
        "Keyframe Extraction",
        keyframes
    )

    run_step(
        "Object Detection",
        objects
    )


    print()
    print("=" * 70)
    print("PHASE 1 COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    main()