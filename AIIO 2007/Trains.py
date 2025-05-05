# https://orac2.info/problem/306/
import heapq
from collections import defaultdict
import sys

sys.stdin = open("trains.in", "r")
sys.stdout = open("trains.out", "w")

n = int(input())
s, f = map(int, input().split())
s -= 1  # 0-based indexing
f -= 1

d = list(map(int, input().split()))
k = int(input())

adj = [[] for _ in range(n)]  # adjacency list: (neighbor, cost)
for _ in range(k):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    adj[x].append((y, c))
    adj[y].append((x, c))

# dist[node][voucher_value] = minimum cost to reach node with given best voucher
dist = [defaultdict(lambda: float('inf')) for _ in range(n)]
# Priority queue: (total_cost, node, current_voucher)
heap = []

dist[s][d[s]] = 0
heapq.heappush(heap, (0, s, d[s]))

while heap:
    cost, u, voucher = heapq.heappop(heap)
    
    if cost > dist[u][voucher]:
        continue
    
    for v, trip_cost in adj[u]:
        new_voucher = max(voucher, d[v])
        adjusted_cost = cost + max(0, trip_cost - voucher)
        
        if adjusted_cost < dist[v][new_voucher]:
            dist[v][new_voucher] = adjusted_cost
            heapq.heappush(heap, (adjusted_cost, v, new_voucher))

print(min(dist[f].values()) if dist[f] else float('inf'))
