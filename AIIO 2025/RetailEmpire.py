n, a, k = map(int, input().split())
cost = [0] * (n + 1)
profit = [0] * (n + 1)

for i in range(1, n + 1):
    cost[i], profit[i] = map(int, input().split())

# Initialize DP table
dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j]
        if j >= cost[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + profit[i])

d = 2
while a + dp[n][a] < k:
    a += dp[n][a]
    d += 1

print(d)