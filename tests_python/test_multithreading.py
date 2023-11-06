import threading
import time
import argparse


def append_to_file(filename, text):
    with open(filename, "a") as file:
        file.write(text)


def heavy_task(id, start_time):
    print(f"Task {id} starting")
    time.sleep(1)
    print(f"Task {id} completed at {time.time() - start_time:.2f}s")


def run_concurrently(num_tasks):
    threads = []
    start_time = time.time()
    print("Running concurrently with threads...")
    for i in range(num_tasks):
        thread = threading.Thread(target=heavy_task, args=(i + 1, start_time))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    print(f"Concurrent execution took: {time.time() - start_time:.2f}s")
    return time.time() - start_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run tasks concurrently.")
    parser.add_argument(
        "-n", "--num-tasks", type=int, default=10, help="Number of tasks"
    )
    args = parser.parse_args()

    timelapse = run_concurrently(args.num_tasks)
    append_to_file("logs/multithreading.log",
                   f"{args.num_tasks},{timelapse}\n")
