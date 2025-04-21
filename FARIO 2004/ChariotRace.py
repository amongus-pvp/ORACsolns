#https://orac2.info/problem/123/

# basically copied this algorithm from Phung Tien Minh's repository for Competetive Programming so show him some love ^^
import heapq

class Edge:
    def __init__(self, to, cost, type):
        self.to = to
        self.cost = cost
        self.type = type

graph = [[] for _ in range(105)]

n = int(input())
start_node, finish_node = map(int, input().split())

m = int(input())
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append(Edge(v, w, 1))

q = int(input())
for _ in range(q):
    u, v = map(int, input().split())
    graph[u].append(Edge(v, 0, 2))

# Dijkstra's algorithm
distances = [float('inf')] * 105
distances[start_node] = 0
priority_queue = []
heapq.heappush(priority_queue, (0, start_node))

while priority_queue:
    current_dist, current_node = heapq.heappop(priority_queue)
    
    if current_dist == distances[current_node]:
        for edge in graph[current_node]:
            neighbor = edge.to
            if edge.type == 1:
                if distances[neighbor] > distances[current_node] + edge.cost:
                    distances[neighbor] = distances[current_node] + edge.cost
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))
            else:
                if distances[neighbor] > distances[current_node] // 2:
                    distances[neighbor] = distances[current_node] // 2
                    heapq.heappush(priority_queue, (distances[neighbor], neighbor))

print(distances[finish_node])
