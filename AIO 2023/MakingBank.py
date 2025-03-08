n = int(input().strip())
d = list(str(input().strip()))
skill = 1
money = 0
for i in range(n):
    if d[i] == 'M':
        money += skill
    else:
        if (skill + 1) * (len(d) - i) > (skill * (len(d) - i + 1)):
            skill += 1
        else:
            money += skill
print(money)