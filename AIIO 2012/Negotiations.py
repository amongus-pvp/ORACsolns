# https://orac2.info/problem/170/
def ok(m, v, k):
    count = 0
    total = v[0]
    rightidx = 0
    ranges = len(v)
 
    for i in range(len(v)):
        if i != 0:
            total -= v[i - 1]
        while total < m:
            ranges -= 1
            rightidx += 1
            if rightidx >= len(v):
                break
            total += v[rightidx]
        if rightidx >= len(v):
            break
        count += ranges
 
    return count >= k
n = int(input())
k = int(input())
v = [int(input()) for _ in range(n)]
l, r = 0, 10**15
ans = 0
 
while l <= r:
    m = (l + r) // 2
    if ok(m, v, k):
        ans = m
        l = m + 1
    else:
        r = m - 1
print(ans)
