import threading
import time
import random

numbers = [
    random.randint(1, 10000)
    for _ in range(10000)
]

results = []
lock = threading.Lock()


def sort_part(data):

    sorted_data = sorted(data)

    with lock:
        results.append(sorted_data)


def run_test(thread_count):

    global results

    results = []

    size = len(numbers) // thread_count

    threads = []

    start = time.time()

    for i in range(thread_count):

        begin = i * size

        if i == thread_count - 1:
            end = len(numbers)
        else:
            end = begin + size

        part = numbers[begin:end]

        thread = threading.Thread(
            target=sort_part,
            args=(part,)
        )

        threads.append(thread)

        thread.start()

    for thread in threads:
        thread.join()

    end = time.time()

    return end - start


print("Thread Performance Analysis")

for count in [1, 2, 4, 8]:

    runtime = run_test(count)

    print(
        count,
        "Thread(s):",
        runtime,
        "seconds"
    )