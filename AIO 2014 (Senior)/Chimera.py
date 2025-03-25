# https://orac2.info/problem/72/
N = int(input())
a = list(input())
b = list(input())
c = list(input())
 
count_a = 0
count_b = 0
count_c = 0
 
ab = 0
bc = 0
ca = 0
 
extras = 0
 
for i in range(N):
    if a[i] != b[i] and b[i] != c[i] and a[i] != c[i]:
        extras += 1
    elif a[i] == b[i] == c[i]:
        count_a += 1
        count_b += 1
        count_c += 1
    else:
        if a[i] == b[i]:
            count_a += 1
            count_b += 1
            ab += 1
        elif c[i] == b[i]:
            count_c += 1
            count_b += 1
            bc += 1
        else:
            count_a += 1
            count_c += 1
            ca += 1
 
 
while extras >= 1 and max(count_a, count_b, count_c) - min(count_a, count_b, count_c) >= 1:
    if count_a == min(count_a, count_b, count_c):
        count_a += 1
        extras -= 1
    elif count_b == min(count_a, count_b, count_c):
        count_b += 1
        extras -= 1
    elif count_c == min(count_a, count_b, count_c):
        count_c += 1
        extras -= 1
 
 
while max(count_a, count_b, count_c) - min(count_a, count_b, count_c) >= 2:
    if count_a == min(count_a, count_b, count_c) and bc >= 1:
        count_a += 1
        bc -= 1
        count_b -= 1
        count_c -= 1
    elif count_b == min(count_a, count_b, count_c) and ca >= 1:
        count_b += 1
        ca -= 1
        count_a -= 1
        count_c -= 1
    elif count_c == min(count_a, count_b, count_c) and ab >= 1:
        count_c += 1
        ab -= 1
        count_b -= 1
        count_a -= 1
 
while extras >= 1:
    if count_a == min(count_a, count_b, count_c):
        count_a += 1
        extras -= 1
    elif count_b == min(count_a, count_b, count_c):
        count_b += 1
        extras -= 1
    elif count_c == min(count_a, count_b, count_c):
        count_c += 1
        extras -= 1
 
print(min(count_a, count_b, count_c))
