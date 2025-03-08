# https://orac2.info/problem/209/
red, blue, spare, redp, bluep = map(int, input().strip().split())
a = 0
if red > redp and blue > bluep:
    if redp == 0:
        a = (blue - bluep + spare + 1)
    elif bluep == 0:
        a = (red - redp + spare + 1)
    else:
        a = (min(red - redp, blue - bluep) + spare + 1)
elif red < redp and blue < bluep:
    a = (spare - (redp - red + bluep - blue) + 1)
else:
    if bluep == 0:
        a = (spare - redp + red + 1)
    elif redp == 0:
        a = (spare - bluep + blue + 1)
    else:
        a = (spare - max(redp - red, bluep - blue) + 1)
print(max(a, 0))