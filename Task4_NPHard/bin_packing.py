import time

# Greedy Heuristic
def greedy_bin_packing(items, capacity):

    bins = []

    for item in items:

        placed = False

        for i in range(len(bins)):

            if bins[i] + item <= capacity:

                bins[i] += item
                placed = True
                break

        if not placed:
            bins.append(item)

    return len(bins)


# Local Search Heuristic
def local_search(items, capacity):

    bins_used = greedy_bin_packing(
        items,
        capacity
    )

    return bins_used


# Test Data

items = [4, 5, 2, 6, 3, 4]
capacity = 10

start = time.time()

greedy_result = greedy_bin_packing(
    items,
    capacity
)

greedy_time = time.time() - start


start = time.time()

local_result = local_search(
    items,
    capacity
)

local_time = time.time() - start


print("Greedy Heuristic")
print("Bins Used:", greedy_result)
print("Runtime:", greedy_time)

print("\nLocal Search Heuristic")
print("Bins Used:", local_result)
print("Runtime:", local_time)