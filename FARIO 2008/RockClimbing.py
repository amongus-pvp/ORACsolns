# https://orac2.info/problem/287/
import heapq
from collections import defaultdict

INF = 10**9

N, R = map(int, input().split())
start = list(map(int, input().split()))
start = [x-1 for x in start]  # convert to 0-based
start.sort()

pos = []
for _ in range(N):
    x, y = map(int, input().split())
    pos.append((x, y))

# Distance function
def dist(i, j):
    return abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])

# Check if every handle in holds is within R of at least one other handle
def is_valid(h):
    for i in range(3):
        ok = False
        for j in range(3):
            if i != j and dist(h[i], h[j]) <= R:
                ok = True
                break
        if not ok:
            return False
    return True

dist_map = {}
heap = []

dist_map[tuple(start)] = 0
heapq.heappush(heap, (0, tuple(start)))

while heap:
    cost, holds = heapq.heappop(heap)
    holds = list(holds)

    if (N-1 in holds):
        print(cost)
        exit()

    for i in range(3):
        old_handle = holds[i]
        for new_handle in range(N):
            if new_handle in holds:
                continue

            next_holds = holds.copy()
            next_holds[i] = new_handle
            next_holds.sort()
            next_holds_tuple = tuple(next_holds)

            if not is_valid(next_holds):
                continue

            new_cost = cost + dist(old_handle, new_handle)
            if next_holds_tuple not in dist_map or new_cost < dist_map[next_holds_tuple]:
                dist_map[next_holds_tuple] = new_cost
                heapq.heappush(heap, (new_cost, next_holds_tuple))

print(-1)  # In case no solution found (though problem likely guarantees one)
