# https://orac2.info/problem/218/
from collections import defaultdict, deque
import heapq
 
N, C, K = map(int, input().split())
toys = []
for i in range(N):
    toys.append(int(input()))
 
future_indices = defaultdict(deque)
 
# Read toy colors and prepare future appearance queues
for i in range(N):
    color = toys[i]
    future_indices[color].append(i)
 
open_tins = set()  # currently open tins
opens = 0
 
# Belady's algorithm
next_use_heap = []
 
for i in range(N):
    color = toys[i]
    future_indices[color].popleft()  # Remove current use
    
    if color in open_tins:
        # Tin already open - do nothing
        pass
    else:
        opens += 1
        
        if len(open_tins) == K:
            # Must evict one
            # Since we can't efficiently remove arbitrary elements from heap,
            # we'll use a lazy approach: check if the top is still in open_tins
            while next_use_heap:
                next_use, to_close = heapq.heappop(next_use_heap)
                next_use = -next_use  # convert back to positive
                if to_close in open_tins:
                    open_tins.remove(to_close)
                    break
            
        open_tins.add(color)
    
    # Push next usage index of current color or N+1 if never again
    next_use = future_indices[color][0] if future_indices[color] else N + 1
    # Using negative for max heap simulation
    heapq.heappush(next_use_heap, (-next_use, color))
 
print(opens)
