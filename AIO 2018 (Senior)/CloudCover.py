# https://orac2.info/problem/154/
n, k = map(int, input().split())
m = 0
p = []
for i in range(n-1):
    p.append(int(input()))
for i in range(k):
    m += p[i]
current = m
for i in range(k, n-1):
    current += p[i]
    current -= p[i - k]
    m = min(m, current)
print(m)
