import math
 
n = int(input())
 
d = math.ceil(math.log(n, 2))
while n%(2**d)!=0:
    d-=1
b = n / (2**d)
 
print(str(int(b)) + " " + str(d))