N = int(input())
 
x = []
y = []
 
for i in range(N):
    Xi, Yi = map(int, input().split())
    x.append(Xi)
    y.append(Yi)
 
print((max(y)-min(y)) * (max(x)-min(x)))