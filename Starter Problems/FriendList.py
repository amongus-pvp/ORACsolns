n = int(input())
 
nu = {}
 
for i in range(n):
    a, b = map(int, input().split())
    if a in nu:
        nu[a] += 1
    else:
        nu[a] = 1
    
    if b in nu:
        nu[b] += 1
    else:
        nu[b] = 1
 
 
ma = 0
for i in nu:
    if nu[i] > ma:
        ma = nu[i]
 
w = []
for i in nu:
    if nu[i] == ma:
        w.append(i)
 
w.sort()
 
for i in w:
    print(i)
