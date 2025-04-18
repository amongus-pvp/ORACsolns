# https://orac2.info/problem/945/
# forgot who i copied this alg from, weird problem
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    adj1 = [[] for _ in range(n)]
    adj2 = [[] for _ in range(n)]
    
    for _ in range(m):
        a = int(data[idx]) - 1
        idx += 1
        b = int(data[idx]) - 1
        idx += 1
        c = int(data[idx])
        idx += 1
        adj1[a].append((b, c))
        adj2[b].append((a, c))
    
    INF = 9999999999
    dist1 = [INF] * n
    dist2 = [INF] * n
    seen1 = [False] * n
    seen2 = [False] * n
    
    # Dijkstra for original graph
    dist1[0] = 0
    heap1 = []
    heapq.heappush(heap1, (0, 0))
    
    while heap1:
        cost, u = heapq.heappop(heap1)
        if seen1[u]:
            continue
        seen1[u] = True
        for (v, c) in adj1[u]:
            if cost + c < dist1[v]:
                dist1[v] = cost + c
                heapq.heappush(heap1, (dist1[v], v))
    
    # Dijkstra for reversed graph
    dist2[0] = 0
    heap2 = []
    heapq.heappush(heap2, (0, 0))
    
    while heap2:
        cost, u = heapq.heappop(heap2)
        if seen2[u]:
            continue
        seen2[u] = True
        for (v, c) in adj2[u]:
            if cost + c < dist2[v]:
                dist2[v] = cost + c
                heapq.heappush(heap2, (dist2[v], v))
    
    # Output the results
    for i in range(1, n):
        if seen1[i] and seen2[i]:
            print(dist1[i] + dist2[i])
        else:
            print(-1)

if __name__ == "__main__":
    main()
