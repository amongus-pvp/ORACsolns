# https://orac2.info/problem/151/
MOD = 1000003

import sys
N, D = map(int, input().split())

# Define adjacency list for each digit
adj = {
    1: [2, 4],
    2: [1, 3, 5],
    3: [2, 6],
    4: [1, 5, 7],
    5: [2, 4, 6, 8],
    6: [3, 5, 9],
    7: [4, 8],
    8: [5, 7, 9],
    9: [6, 8]
}

if N == 1:
    print(1)
    exit()

# Initialize DP arrays
prev_dp = [0] * 10
prev_dp[D] = 1

for _ in range(2, N + 1):
    curr_dp = [0] * 10
    for d in range(1, 10):
        if prev_dp[d] == 0:
            continue
        for neighbor in adj[d]:
            curr_dp[neighbor] = (curr_dp[neighbor] + prev_dp[d]) % MOD
    prev_dp = curr_dp

total = sum(prev_dp) % MOD
print(total)
