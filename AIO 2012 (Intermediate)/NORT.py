# https://orac2.info/problem/303/
W, H = map(int, input().split())
 
if W%2==0 or H%2==0:
    print(W*H)
else:
    print((W*H)-1)
