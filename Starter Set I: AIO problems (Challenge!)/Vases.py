# https://orac2.info/problem/3/
N = int(input())
 
if N <= 5:
    print("0 0 0")
else:
    print("1 2 " + str(N-3))
