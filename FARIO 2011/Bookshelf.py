# https://orac2.info/problem/292/
from collections import deque
def solve():
    N, M, I = map(int, input().split())
    heights = list(map(int, input().split()))
    infected_indices = list(map(lambda x: int(x) - 1, input().split()))
    irreplaceable = set(map(lambda x: int(x) - 1, input().split()))

    infected = [False] * N
    queue = deque()
     
    # Initially infected books
    for idx in infected_indices:
        infected[idx] = True
        queue.append(idx)
     
    while queue:
        i = queue.popleft()
        # Spread left
        if i > 0 and not infected[i - 1] and heights[i - 1] >= heights[i]:
            infected[i - 1] = True
            queue.append(i - 1)
        # Spread right
        if i < N - 1 and not infected[i + 1] and heights[i + 1] >= heights[i]:
            infected[i + 1] = True
            queue.append(i + 1)
     
    count = sum(1 for idx in irreplaceable if infected[idx])
    print(count)

solve()
