# https://orac2.info/problem/1084/
import bisect

import sys
sys.stdin = open("pairsin.txt", "r")
sys.stdout = open("pairsout.txt", "w")

input = sys.stdin.read
data = input().split()

idx = 0
n = int(data[idx])
idx += 1
a = int(data[idx])
idx += 1
b = int(data[idx])
idx += 1

v = []
for _ in range(n):
    v.append(int(data[idx]))
    idx += 1

v.sort()
ans = 0

for i in range(n):
    low = a - v[i]
    high = b - v[i]
    lb = bisect.bisect_left(v, low)
    ub = bisect.bisect_right(v, high)
    ans += (ub - lb)
    if low <= v[i] <= high:
        ans -= 1

print(ans // 2)
