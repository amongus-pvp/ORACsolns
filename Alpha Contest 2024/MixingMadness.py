# https://orac2.info/problem/1374/
from collections import defaultdict

N = int(input())
shades = list(map(int, input().split()))
K = int(input())
allowed_shades = list(map(int, input().split()))
allowed_set = set(allowed_shades)

# Initialize data structures
last_seen = [defaultdict(int) for _ in range(K)]
dp = [-1] * (N + 1)
dp[0] = 0

# Initialize modified prefix sums for each allowed shade
for k in range(K):
    last_seen[k][0] = 0

prefix_sum = 0
for i in range(1, N + 1):
    prefix_sum += shades[i-1]
    
    for k in range(K):
        p = allowed_shades[k]
        modified = prefix_sum - p * i
        
        if modified in last_seen[k]:
            j = last_seen[k][modified]
            if dp[j] != -1:
                dp[i] = j
                break
    
    if dp[i] != -1:
        for k in range(K):
            p = allowed_shades[k]
            modified = prefix_sum - p * i
            last_seen[k][modified] = i

if dp[N] != -1:
    print("POSSIBLE")
    
    # Reconstruct the solution
    ranges = []
    current = N
    while current > 0:
        ranges.append((dp[current] + 1, current))
        current = dp[current]
    
    ranges.reverse()
    print(len(ranges))
    for l, r in ranges:
        print(l, r)
else:
    print("IMPOSSIBLE")
