import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination, weight):

        if source not in self.graph:
            self.graph[source] = []

        self.graph[source].append(
            (destination, weight)
        )

    def display(self):

        for city in self.graph:
            print(
                city,
                "->",
                self.graph[city]
            )

    def dijkstra(self, start):

        distances = {
            city: float('inf')
            for city in self.graph
        }

        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:

            current_distance, current_city = (
                heapq.heappop(priority_queue)
            )

            if current_distance > distances[current_city]:
                continue

            for neighbor, weight in self.graph[current_city]:

                distance = (
                    current_distance + weight
                )

                if distance < distances.get(
                    neighbor,
                    float('inf')
                ):

                    distances[neighbor] = distance

                    heapq.heappush(
                        priority_queue,
                        (distance, neighbor)
                    )

        return distances


# Test Code

g = Graph()

g.add_edge("Kathmandu", "Pokhara", 200)
g.add_edge("Kathmandu", "Butwal", 250)
g.add_edge("Pokhara", "Biratnagar", 300)

g.graph["Butwal"] = []
g.graph["Biratnagar"] = []

print("Transportation Network:")
g.display()

print("\nShortest Paths from Kathmandu:")

result = g.dijkstra("Kathmandu")

for city, distance in result.items():
    print(city, ":", distance)
