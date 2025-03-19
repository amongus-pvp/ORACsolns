# https://orac2.info/problem/261/
N = int(input())
 
p = [int(input()) for _ in range(N)]
 
output = 0
 
l = r = 0
 
on_table = -p[0]
 
while not(l % N == (r + 1) % N):
    if on_table < 0:
        l -= 1
        on_table -= p[l % N]
    else:
        r += 1
        on_table -= p[r % N]
 
output = (l % N) + 1
 
print(output)
