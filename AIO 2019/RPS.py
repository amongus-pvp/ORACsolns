# https://orac2.info/problem/112/
Ra, Pa, Sa = map(int, input().split())
Rb, Pb, Sb = map(int, input().split())

w1 = min(Ra,Pb) # calculate maximum wins
w2 = min(Pa,Sb)
w3 = min(Sa,Rb)
 
answer = w1 + w2 + w3 # subtract all the wins
Ra -= w1
Pb -= w1
Pa -= w2
Sb -= w2
Sa -= w3
Rb -= w3
 
d1 = min(Ra,Rb) # calculate maximum draws
d2 = min(Pa,Pb)
d3 = min(Sa,Sb)
 
Ra -= d1 # subtratc all draws
Rb -= d1
Pa -= d2
Pb -= d2
Sa -= d3
Sb -= d3
 
answer -= Rb + Pb + Sb # rest must be losses
print(answer)
