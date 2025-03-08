D, T = map(int, input().split())
a = []
b = []
for i in range(T):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
 
da = [0 for i in range(D)]
 
# wow
 
for i in range(T):
    if da[a[i] - 1] == 0:
        da[a[i] - 1] += 1
    
    da[a[i] - 1] -= 1
    da[b[i] - 1] += 1
 
print(sum(da))