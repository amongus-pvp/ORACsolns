# https://orac2.info/problem/1100/
N = int(input())
A = input()
B = input()
 
# trans rights
cur_length = 0
 
ans = 0
 
for i in range(2*N):
    if A[i] == 'D' and B[i] == 'R':
        cur_length = cur_length + 1
 
    if A[i] == 'R' and B[i] == 'D':
        cur_length = cur_length - 1
 
    ans = max(ans, cur_length)
 
print(ans)