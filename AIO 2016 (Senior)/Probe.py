# https://orac2.info/problem/75/
import math
 
def dist(x1, y1, x2, y2):
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return x * x + y * y
 
r, c, rp, cp, rf, cf = map(int, input().split())
q = int(input())
ans = []

for _ in range(q):
    x, y = map(int, input().split())
    if abs(cf - cp) == abs(rf - rp):
        if dist(x, y, rp, cp) < dist(x, y, rf, cf):
            out = "WATER"
        elif dist(x, y, rp, cp) > dist(x, y, rf, cf):
            out = "LAVA"
        else:
            out = "MOUNTAINS"
    else:
        waterdist = abs(x - rp) + abs(y - cp)
        lavadist = abs(x - rf) + abs(y - cf)
        if waterdist < lavadist:
            out = "WATER"
        elif waterdist > lavadist:
            out = "LAVA"
        else:
            out = "MOUNTAINS"
    ans.append(out)

for result in ans:
    print(result)
