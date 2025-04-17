# https://orac2.info/problem/1138/
import sys
sys.setrecursionlimit(1 << 25)
 
n = int(input())
profit = [0] + list(map(int, input().split()))  # 1-based indexing
tree = [[] for _ in range(n + 1)]
 
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
 
max_profit = -float('inf')
 
def dfs(u, parent):
    global max_profit
    total = profit[u]
    for v in tree[u]:
        if v != parent:
            child_sum = dfs(v, u)
            if child_sum > 0:
                total += child_sum
    max_profit = max(max_profit, total)
    return total
 
dfs(1, 0)
print(max_profit)
