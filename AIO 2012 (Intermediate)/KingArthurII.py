# https://orac2.info/problem/117/
import sys
from collections import deque

def solve():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    P = int(input[ptr])
    ptr += 1

    adj = [[] for _ in range(N + 1)]
    for _ in range(P):
        a = int(input[ptr])
        b = int(input[ptr + 1])
        adj[a].append(b)
        adj[b].append(a)
        ptr += 2

    color = [-1] * (N + 1)
    max_size = 0

    for i in range(1, N + 1):
        if color[i] == -1:
            queue = deque()
            queue.append(i)
            color[i] = 0
            count = [0, 0]
            count[0] += 1
            is_bipartite = True

            while queue and is_bipartite:
                u = queue.popleft()
                for v in adj[u]:
                    if color[v] == -1:
                        color[v] = color[u] ^ 1
                        count[color[v]] += 1
                        queue.append(v)
                    elif color[v] == color[u]:
                        is_bipartite = False
                        break

            if is_bipartite:
                max_size += max(count[0], count[1])

    print(max_size)

solve()
