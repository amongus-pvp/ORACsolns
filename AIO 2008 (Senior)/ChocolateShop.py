# https://orac2.info/problem/21/
# this problem is ridiculously easy for some reason
# REASON?
N = int(input())
rsum = 0
 
for i in range(N):
    x = int(input())
    rsum += x
    if rsum >= 10:
        rsum -= 10
 
if rsum != 0:
    print(10 - rsum)
else:
    print(0)
