# https://orac2.info/problem/165/
# had to take another persons soln here cus i was too lazy to rewrite my C++

x = []
s = []
m = []
 
n = int(input())
for _ in range(n):
    k = int(input())
    x.append(k)
 
n = int(input())
for _ in range(n):
    k = int(input())
    s.append(k)
 
n = int(input())
for _ in range(n):
    k = int(input())
    m.append(k)
 
x = sorted(x)
s = sorted(s)
m = sorted(m)
 
cr = 0
xi = 0
for it in s:
    if xi >= len(x):
        break
    if x[xi] <= it:
        cr += 1
        xi += 1
 
mk = 0
for xi in range(xi, len(x)):
    if mk >= len(m):
        break
    if x[xi] >= m[mk]:
        cr += 1
        mk += 1
 
print(cr)
