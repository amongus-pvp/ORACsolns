# https://orac2.info/problem/1224/
import heapq

INF = float('inf')

def solve():
    V, E, K = map(int, input().split())
    grounded = list(map(int, input().split()))

    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, d = map(int, input().split())
        adj[a].append((b, d))
        adj[b].append((a, d))

    dist = [INF] * (V + 1)
    source = [-1] * (V + 1)

    # Priority queue (min-heap)
    pq = []
    
    # Initialize with all grounded nodes
    for g in grounded:
        dist[g] = 0
        source[g] = g
        heapq.heappush(pq, (0, g))

    answer = INF

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in adj[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                source[v] = source[u]
                heapq.heappush(pq, (dist[v], v))
            elif source[v] != source[u]:  # Found a path between different grounded terminals
                answer = min(answer, dist[u] + dist[v] + w)

    print(answer)

solve()
