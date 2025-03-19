# https://orac2.info/problem/147/
import bisect
 
n, m, l = map(int, input().strip().split())
 
stores = list(map(int, input().strip().split()))
houses = list(map(int, input().strip().split()))
pham = list(map(int, input().strip().split()))
 
# Store the required distances in a dictionary.
p = {i: pham[i] for i in range(m)}
 
# Initialize the binary search bounds.
low, high = 0, l
 
while low <= high:
    mid = (low + high) // 2
    dist = []
 
    # Calculate the number of stores within the distance `mid` for each house.
    for i in range(m):
        start = bisect.bisect_left(stores, houses[i] - mid)
        end = bisect.bisect_right(stores, houses[i] + mid)
        dist.append(end - start)
 
    dist.sort()
    found = False
 
    for i in range(m):
        if dist[i] > p[i]:
            high = mid - 1
            found = True
            break
        elif dist[i] < p[i]:
            low = mid + 1
            found = True
            break
 
    # If a valid distance is found, print the result and exit.
    if not found:
        print(mid)
        break
 
# If no valid distance was found, print `-1`.
if found:
    print(-1)
