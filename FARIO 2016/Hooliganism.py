# https://orac2.info/problem/105/
import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    deg = [0] * (n + 1)
    g = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    
    # Read initial degrees
    for i in range(1, n + 1):
        x = int(sys.stdin.readline())
        deg[i] += x
    
    # Read edges and update degrees
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] -= 1
        deg[v] -= 1
    
    q = deque()
    for i in range(1, n + 1):
        if deg[i] >= 0:
            q.append(i)
    
    ans = []
    
    while q:
        u = q.popleft()
        visited[u] = True
        for v in g[u]:
            if visited[v]:
                continue
            ans.append((u, v))
            deg[v] += 1
            if deg[v] == 0:
                q.append(v)
    
    if len(ans) != m:
        print("IMPOSSIBLE")
    else:
        for edge in ans:
            print(edge[0], edge[1])

if __name__ == "__main__":
    main()
