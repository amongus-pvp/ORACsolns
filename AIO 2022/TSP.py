n = int(input().strip())
l = list(map(int, input().strip().split()))
r = list(map(int, input().strip().split()))
mustsell = l[0]
q = 0
for i in range(n):
    if r[i] < mustsell:
        q = 1
    elif l[i] > mustsell:
        mustsell = l[i]
if q == 0:
    print('YES')
else:
    print('NO')