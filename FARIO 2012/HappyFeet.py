# https://orac2.info/problem/157/
N, M = map(int, input().split())
 
trails = []
for _ in range(M):
    u, v, p = map(int, input().split())
    trails.append((u, v, p))
 
# Sort trails by penguin count
trails.sort(key=lambda x: x[2])
 
dp = [0] * (N + 1)  # dp[1..N]
updates = []
 
i = 0
while i < M:
    current_p = trails[i][2]
    updates.clear()
    while i < M and trails[i][2] == current_p:
        u, v, p = trails[i]
        new_value = dp[u] + p
        updates.append((v, new_value))
        if u != v:
            new_value = dp[v] + p
            updates.append((u, new_value))
        i += 1
    for v, value in updates:
        if value > dp[v]:
            dp[v] = value
 
max_penguins = max(dp[1:N+1])
print(max_penguins)
