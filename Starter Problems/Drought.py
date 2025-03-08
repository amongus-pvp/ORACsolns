n, c = map(int, input().split())
d = 0
count = 0
for x in range(c):
    count += int(input())
    d += 1
    if count >= c:
        break
print(d)
