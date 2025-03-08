N = int(input())

count = 0
 
while N >= 100:
    N-=100
    count += 1
while N>=20:
    N-=20
    count += 1
while N>=5:
    N-=5
    count += 1
while N>=1:
    N-=1
    count += 1

print(count)