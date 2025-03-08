N, K = map(int, input().split())
S = 0
 
while N > 0:
    N -= 1 # capturing 1
    S += K
    N -= K
 
S += N # making up for any overflow, e.g if N becomes -2
print(S)
