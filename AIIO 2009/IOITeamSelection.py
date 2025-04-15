# https://orac2.info/problem/102/
import sys
sys.stdin = open("teamin.txt", "r")
sys.stdout = open("teamout.txt", "w")

def solve(n, k, x):
    res = (k - 1) % (n - x + 1)  # base case
    for i in range(n - x + 2, n + 1):  # simulate the recurrence x-1 more times
        res = (res + k) % i
    return res


n, k = map(int, input().split())
answers = [
    solve(n, k, n - 3) + 1,
    solve(n, k, n - 2) + 1,
    solve(n, k, n - 1) + 1,
    solve(n, k, n) + 1
]
print(" ".join(map(str, answers)))
