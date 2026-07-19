import threading
import time

numbers = [45, 12, 78, 23, 56, 89, 11, 67]

lock = threading.Lock()
sorted_parts = []


def sort_part(data):

    local_sorted = sorted(data)

    with lock:
        sorted_parts.append(local_sorted)


# Sequential Sorting
start = time.time()

sequential_result = sorted(numbers)

sequential_time = time.time() - start

print("Sequential Sort:")
print(sequential_result)
print("Time:", sequential_time)


# Concurrent Sorting
mid = len(numbers) // 2

part1 = numbers[:mid]
part2 = numbers[mid:]

start = time.time()

t1 = threading.Thread(
    target=sort_part,
    args=(part1,)
)

t2 = threading.Thread(
    target=sort_part,
    args=(part2,)
)

t1.start()
t2.start()

t1.join()
t2.join()

concurrent_result = sorted(
    sorted_parts[0] + sorted_parts[1]
)

concurrent_time = time.time() - start

print("\nConcurrent Sort:")
print(concurrent_result)
print("Time:", concurrent_time)