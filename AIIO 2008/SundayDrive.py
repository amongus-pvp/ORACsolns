# https://orac2.info/problem/163/
from collections import defaultdict, deque
import sys
INF = int(1e9)

sys.stdin = open("drivein.txt", "r")
sys.stdout = open("driveout.txt", "w")

S = int(input())
song = list(map(int, input().split()))
N, H = map(int, input().split())
T = int(input())

graph = defaultdict(list)
for _ in range(T):
    u, v, m = map(int, input().split())
    graph[u].append((v, m))
    graph[v].append((u, m))

# Initialize DP table
dp = [[INF] * (N + 1) for _ in range(S + 1)]
dp[0][H] = 0

# Dynamic programming over the graph
for s in range(S):
    for u in range(1, N + 1):
        if dp[s][u] == INF:
            continue
        for v, m in graph[u]:
            cost = 0 if m == song[s] else 1
            dp[s + 1][v] = min(dp[s + 1][v], dp[s][u] + cost)

print(dp[S][H])
