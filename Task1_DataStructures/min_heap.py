import heapq


class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, distance, city):
        heapq.heappush(
            self.heap,
            (distance, city)
        )
    def get_next_city(self):
        return heapq.heappop(self.heap)
heap = MinHeap()

if __name__ == "__main__":

    heap = MinHeap()

    heap.insert(200, "Pokhara")
    heap.insert(0, "Kathmandu")
    heap.insert(250, "Butwal")

    print("Heap Contents:")

    print(heap.heap)

    next_city = heap.get_next_city()

    print("\nNext City to Visit:")

    print(next_city)