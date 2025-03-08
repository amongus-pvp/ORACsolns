n = int(input().strip())
p = list(map(int, input().split()))

aC = [0] * 100001
lAC = [0] * n

for i in range(n):
    note = p[i]
    lAC[i] = aC[note] = aC[note - 1] + 1

lC = 0
dC = [0] * 100001
lDC = [0] * n

for i in range(n):
    oN = p[n - i - 1]
    lDC[i] = dC[oN] = dC[oN - 1] + 1

for i in range(n):
    lC = max(lC, min(lAC[i], lDC[n - i - 1]))

print(n - 2 * lC + 1)