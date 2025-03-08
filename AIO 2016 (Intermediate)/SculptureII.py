# https://orac2.info/problem/139/
class Sech:
    def __init__(self, h, ts, te):
        self.h = h
        self.ts = ts
        self.te = te
# OOP vomit
n = int(input())
cr = 0
se = []
 
for _ in range(n):
    t, w, h = map(int, input().split())
    t -= 1
    while se and t >= se[-1].te:
        se.pop()
    se.append(Sech((se[-1].h if se else 0) + h, t, t + w))
    cr = max(cr, se[-1].h if se else 0)
 
print(cr)