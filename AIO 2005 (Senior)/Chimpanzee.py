# https://orac2.info/problem/98/
x, y = map(int, input().split())
square = max(abs(x), abs(y)) * 2 + 1
br = square * square
bl = square * square - square + 1
tl = bl - square + 1
tr = tl - square + 1
 
if x == max(abs(x), abs(y)) and y != -1 * max(abs(x), abs(y)):
    ans = tr - (max(abs(x), abs(y)) - y)
elif -1 * x == max(abs(x), abs(y)):
    ans = bl - abs(max(abs(x), abs(y)) + y)
elif -1 * y == max(abs(x), abs(y)):
    ans = br - (max(abs(x), abs(y)) - x)
else:
    ans = tl - abs(max(abs(x), abs(y)) + x)
 
print(ans - 1)
