n = int(input().strip())
buildings = list(map(int, input().strip().split()))
ugly = 0
potential = [0]
 
for i in range(n - 1):
    ugly += abs(buildings[i] - buildings[i + 1])
potential.append(abs(buildings[0] - buildings[1]))
potential.append(abs(buildings[-1] - buildings[-2]))
 
for i in range(n - 2):
    if buildings[i] > buildings[i + 1] > buildings[i + 2] or buildings[i] < buildings[i + 1] < buildings[i + 2]:
        potential.append(0)
    else:
        potential.append(2*(min(abs(buildings[i + 1] - buildings[i]), abs(buildings[i + 1] - buildings[i + 2]))))
 
print(ugly - max(potential))