d, c0 = map(int, input().strip().split())
p1, c1 = map(int, input().strip().split())
p2, c2 = map(int, input().strip().split())
rate = c0
cookies = 0
q = 0
amogus = [d * rate]
 
for i in range(d):
    cookies += rate
    if cookies >= p1 and q == 0:
        cookies -= p1
        rate += c1
        q += 1
 
amogus.append(cookies)
 
rate = c0
cookies = 0
q = 0
for i in range(d):
    cookies += rate
    if cookies >= p2 and q == 0:
        cookies -= p2
        rate += c2
        q += 1
amogus.append(cookies)
rate = c0
cookies = 0
q = 0
 
for i in range(d):
    cookies += rate
    if cookies >= p1 and q == 0:
        cookies -= p1
        rate += c1
        q += 1
    if cookies >= p2 and q == 1:
        cookies -= p2
        rate += c2
        q += 1
amogus.append(cookies)
rate = c0
cookies = 0
q = 0
 
for i in range(d):
    cookies += rate
    if cookies >= p2 and q == 0:
        cookies -= p2
        rate += c2
        q += 1
    if cookies >= p1 and q == 1:
        cookies -= p1
        rate += c1
        q += 1
 
amogus.append(cookies)
print(max(amogus))