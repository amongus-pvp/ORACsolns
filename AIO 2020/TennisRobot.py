# https://orac2.info/problem/216/
line = input().strip()
B, N = map(int, line.split())
bins = list(map(int, input().strip().split()))
i = 0
B_next = B
result = 0
 
while N > 0:
    avg = max(N//B_next, 1)
 
    for i in range(B):
        if bins[i] > 0:
            s = min(bins[i], avg)
            bins[i] -= s
            N -= s
 
            if bins[i] == 0:
                B_next -= 1
 
        if N == 0:
            result = i + 1
            break
 
print(result)