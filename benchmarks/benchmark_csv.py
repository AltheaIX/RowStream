import os
import time
import tracemalloc

from dataset.repository.csv_repository import CSVDatasetRepository


def measure(fn):
    tracemalloc.start()

    t0 = time.perf_counter()
    result = fn()
    t1 = time.perf_counter()

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "time": t1 - t0,
        "peak_memory": peak
    }


repo = CSVDatasetRepository("dataset_full.csv")

if __name__ == "__main__":
    print(">>> FULL READ")
    print(measure(lambda: repo.get_all_rows()))

    print("\n>>> OFFSET READ")
    print(measure(lambda: repo.read_csv(limit=10, offset=9999)))

    print("\n>>> BUILD INDEX")
    print(measure(lambda: repo.load_index()))

    print("\n>>> OFFSET READ (WITH INDEXING)")
    print(measure(lambda: repo.read_csv_with_seek(repo.index[len(repo.index)-1])))