from collections import deque

def bfs(N, graph, bandwidth, K, D, L):
    # BFS to check if we can reach at least K stations with message length L
    visited = [-1] * (N + 1)  # visited[node] = minimum number of links to reach this node
    queue = deque([1])  # start BFS from station 1
    visited[1] = 0  # station 1 is visited with 0 links

    reachable = 0  # count of reachable stations

    while queue:
        u = queue.popleft()
        current_links = visited[u]
        
        # Count if the current node satisfies the bandwidth constraint
        if bandwidth[u - 1] >= L:
            reachable += 1
        
        # Traverse neighbors (adjacent stations)
        for v in graph[u]:
            if visited[v] == -1 and bandwidth[v - 1] >= L and current_links + 1 <= D:
                visited[v] = current_links + 1
                queue.append(v)
    
    return reachable >= K

def solve():
    N, M, K, D = map(int, input().split())
    bandwidth = list(map(int, input().split()))
    edges = [tuple(map(int, input().split())) for _ in range(M)]
    graph = {i: [] for i in range(1, N + 1)}
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # Binary search for the longest message length L
    low, high = 1, max(bandwidth)
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        if bfs(N, graph, bandwidth, K, D, mid):
            answer = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return answer

import sys
sys.stdin = open("radin.txt", "r")
sys.stdout = open("radout.txt", "w")
print(solve())
