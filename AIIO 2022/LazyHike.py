# https://orac2.info/problem/1140/
import heapq
 
def lazy_hike(N, A, B, heights, trails):
    from collections import defaultdict
 
    graph = defaultdict(list)
    for u, v in trails:
        h1, h2 = heights[u - 1], heights[v - 1]
        graph[u].append((v, h1, h2))
        graph[v].append((u, h2, h1))
 
    # (uphill, downhill, node)
    heap = [(0, 0, 1)]
    visited = dict()  # visited[node] = (min_uphill, min_downhill)
 
    while heap:
        up, down, node = heapq.heappop(heap)
 
        if node in visited:
            prev_up, prev_down = visited[node]
            if up > prev_up and down > prev_down:
                continue
            if up >= prev_up and down >= prev_down:
                continue  # worse or equal path
        visited[node] = (up, down)
 
        for nei, h_curr, h_nei in graph[node]:
            if h_nei > h_curr:
                up_cost = h_nei - h_curr
                down_cost = 0
            else:
                up_cost = 0
                down_cost = h_curr - h_nei
 
            new_up = up + up_cost
            new_down = down + down_cost
 
            if new_up <= A and new_down <= B:
                heapq.heappush(heap, (new_up, new_down, nei))
 
    return len(visited)
 
# Input handling
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
 
    idx = 0
    N = int(data[idx]); idx += 1
    A = int(data[idx]); idx += 1
    B = int(data[idx]); idx += 1
 
    heights = list(map(int, data[idx:idx+N]))
    idx += N
 
    M = int(data[idx]); idx += 1
    trails = []
    for _ in range(M):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        trails.append((u, v))
 
    print(lazy_hike(N, A, B, heights, trails))
 
if __name__ == "__main__":
    main()
