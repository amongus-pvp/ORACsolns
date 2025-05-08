# https://orac2.info/problem/110/
import sys
sys.stdin = open('jogin.txt')
sys.stdout = open('jogout.txt', 'w')

from collections import defaultdict, deque

# Read number of landmarks
L = int(input())

# Build graph
graph = defaultdict(list)
in_degree = [0] * (L + 1)

while True:
    A, B, E = map(int, input().split())
    if A == 0 and B == 0 and E == 0:
        break
    graph[A].append((B, E))
    in_degree[B] += 1

# Topological sort using Kahn's algorithm
queue = deque()
for node in range(1, L + 1):
    if in_degree[node] == 0:
        queue.append(node)

topo_order = []
while queue:
    node = queue.popleft()
    topo_order.append(node)
    for nei, _ in graph[node]:
        in_degree[nei] -= 1
        if in_degree[nei] == 0:
            queue.append(nei)

# Initialize distances
dp = [-float('inf')] * (L + 1)
for node in range(1, L + 1):
    dp[node] = 0  # Allow starting from any node

# Longest path DP
for node in topo_order:
    for nei, w in graph[node]:
        if dp[nei] < dp[node] + w:
            dp[nei] = dp[node] + w

# Output max benefit
print(max(dp))
