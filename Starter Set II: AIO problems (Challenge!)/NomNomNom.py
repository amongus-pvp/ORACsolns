N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

count = 1
num = arr[0]
arr.pop(0)
l = 0
r = 0
while l<N-1 and r<N-1:
    s = sum(arr[l:r+1])
    if s < num:
        r += 1
    elif s >= num:
        count += 1
        l = r+1
        r += 1
        num = s

print(count)