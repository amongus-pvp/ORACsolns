# https://orac2.info/problem/1135/
from collections import deque

N = int(input())
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# Find the furthest node from 1
dist = [-1] * (N + 1)
q = deque()
q.append(1)
dist[1] = 0
while q:
    u = q.popleft()
    for v in adj[u]:
        if dist[v] == -1:
            dist[v] = dist[u] + 1
            q.append(v)

max_dist = 0
furthest_node = 1
for i in range(1, N + 1):
    if dist[i] > max_dist:
        max_dist = dist[i]
        furthest_node = i

# The answer is 2*(N-1) - max_dist + 1 (since edges are N-1)
print(2 * (N - 1) - max_dist + 1)
