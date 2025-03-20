# https://orac2.info/problem/104/
N, W = map(int, input().split())
 
psum = [int(input())] # prefix sum :D
 
for i in range(1, N):
    psum.append(psum[i-1] + int(input()))
m = psum[W - 1]
# simply create a sliding window now
for i in range(1, N - W + 1):
    m = max(m, psum[i + W - 1] - psum[i-1])
print(m)
