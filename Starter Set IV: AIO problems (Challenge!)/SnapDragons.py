R, S = map(int, input().split())
r, s = [], []
sc = {}
for i in range(R):
    r.append(int(input()))
for i in range(S):
    x = int(input())
    s.append(x)
    if x in sc:
        sc[x] += 1
    else:
        sc[x] = 1
 
pairs = 0
for i in r:
    if i in sc:
        pairs += sc[i]
print(pairs)