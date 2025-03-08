# https://orac2.info/problem/1463/
N = int(input())
throws = list(map(int, input().split()))
 
maxt = -1
ans = 0
    
for t in throws:
    if t > maxt:
        ans += 1
        maxt = t
 
print(ans)