# https://orac2.info/problem/331/
f = int(input())
d = 0
n = f
 
while (n-1)%11!=0:
    n = n*2
    d += 1

print(d, n)
