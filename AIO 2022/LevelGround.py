# https://orac2.info/problem/1195/
n = int(input().strip())
alts = list(map(int, input().strip().split()))
 
maxintensity = 0
current = 0
last = -1
 
for i in range(n):
    if last != alts[i]:
        current = 0
    current += alts[i]
    last = alts[i]
    if current > maxintensity:
        maxintensity = current
 
print(maxintensity)