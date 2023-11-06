import multiprocessing
import time
import argparse


def append_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text)


def heavy_task(id):
    print(f"Task {id} starting")
    time.sleep(1)
    return f"Task {id} completed"


def run_in_parallel(num_tasks):
    pool = multiprocessing.Pool()
    start_time = time.time()
    print("Running in parallel with processes...")
    results = pool.map(heavy_task, range(1, num_tasks + 1))
    for result in results:
        print(result + f" at {time.time() - start_time:.2f}s")
    pool.close()
    pool.join()
    print(f"Parallel execution took: {time.time() - start_time:.2f}s")
    return time.time() - start_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tasks concurrently.")
    parser.add_argument(
        "-n", "--num-tasks", type=int, default=10, help="Number of tasks"
    )
    args = parser.parse_args()
    timelapse = run_in_parallel(args.num_tasks)
    append_to_file("logs/multiprocessing.log",
                   f"{args.num_tasks},{timelapse}\n")
