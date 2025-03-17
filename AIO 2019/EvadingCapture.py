# https://orac2.info/problem/106/
from collections import deque

n, e, x, k = map(int, input().split())
neighbours = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b = map(int, input().split())
    neighbours[a].append(b)
    neighbours[b].append(a)

# Initialize even and odd distances
even = [float('inf')] * (n + 1)
odd = [float('inf')] * (n + 1)
even[x] = 0  # Starting node has even distance 0

# BFS setup
queue = deque()
for neighbor in neighbours[x]:
    odd[neighbor] = 1
    queue.append((neighbor, 1))  # (node, depth)

# BFS traversal
while queue:
    node, depth = queue.popleft()
    for neighbor in neighbours[node]:
        if depth + 1 < even[neighbor] if (depth + 1) % 2 == 0 else depth + 1 < odd[neighbor]:
            if (depth + 1) % 2 == 0:
                even[neighbor] = depth + 1
            else:
                odd[neighbor] = depth + 1
            queue.append((neighbor, depth + 1))

# Count reachable nodes
ans = 0
if k % 2 == 0:
    for i in range(1, n + 1):
        if even[i] <= k:
            ans += 1
else:
    for i in range(1, n + 1):
        if odd[i] <= k:
            ans += 1

print(ans)
