# https://orac2.info/problem/220/
a, b, c = map(int, input().split())
 
print(max(a-((a-b)+(a-c)),1), min(b-1+c,a))
