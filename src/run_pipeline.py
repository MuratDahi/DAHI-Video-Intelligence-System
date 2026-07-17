import time

from run_phase1 import main as phase1
from run_phase2 import main as phase2


def main():

    total_start = time.time()

    print()
    print("=" * 70)
    print("DAHI MULTIMODAL AI PIPELINE")
    print("=" * 70)

    phase1()

    phase2()

    total = time.time() - total_start

    print()
    print("=" * 70)
    print("DAHI PIPELINE COMPLETED")
    print("=" * 70)

    print()

    print(f"Total Time : {total:.2f} seconds")


if __name__ == "__main__":
    main()