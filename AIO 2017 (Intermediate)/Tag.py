# https://orac2.info/problem/225/
N, M = map(int, input().split())
tags = [tuple(map(int, input().split())) for _ in range(M)]
 

red_team = {1} # using sets for teams because super fast lookup
blue_team = {2}
 
# Process tags
for a, b in tags:
    if a in red_team:
        red_team.add(b)
    elif a in blue_team:
        blue_team.add(b)

print(len(red_team), len(blue_team))
