# https://orac2.info/problem/1143/
from collections import deque
import sys
 
def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
# fun graph problem lol
input = sys.stdin.read
data = input().split()
idx = 0
N = int(data[idx])
idx += 1
M = int(data[idx])
idx += 1
adj = [[] for _ in range(N + 1)]
reverse_adj = [[] for _ in range(N + 1)]
for _ in range(M):
    a = int(data[idx])
    idx += 1
    b = int(data[idx])
    idx += 1
    adj[a].append(b)
    reverse_adj[b].append(a)
from_1 = [False] * (N + 1)
to_N = [False] * (N + 1)
bfs(1, adj, from_1)
bfs(N, reverse_adj, to_N)
count = 0
for i in range(1, N + 1):
    if from_1[i] and to_N[i]:
        count += 1
print(count)
