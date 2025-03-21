# https://orac2.info/problem/295/
N = int(input())
cost = [int(input()) for d in range(N)]
lst0, lst1, lst2, lst3, lst4 = [],[],[],[],[]
total = 0
def rounder(n):
    temp = n%5
    if temp == 0:
        return n
    elif temp <= 2:
        return n-temp
    else:
        temp = 5-temp
        return n + temp
for i in range (N):
    if cost[i]%5 == 0:
        lst0.append(cost[i])
    elif cost[i]%5 == 1:
        lst1.append(cost[i])
    elif cost[i]%5 == 2:
        lst2.append(cost[i])
    elif cost[i]%5 == 3:
        lst3.append(cost[i])
    else:
        lst4.append(cost[i])
 
pair3and4 = min(len(lst3), len(lst4))
for i in range(pair3and4):
    total += rounder(lst3.pop() + lst4.pop())
 
while len(lst3) >= 4:
    total += rounder(lst3.pop() + lst3.pop()+ lst3.pop()+ lst3.pop())
 
while len(lst3) >= 2:
    total += rounder(lst3.pop() + lst3.pop())
    
if len(lst3) == 1:  
    total += rounder(lst3.pop())
 
while len(lst4) >= 3:
    total += rounder(lst4.pop() + lst4.pop()+lst4.pop())
    
while len(lst4) >= 4:
    total += rounder(lst4.pop() + lst4.pop()+lst4.pop() + lst4.pop())
 
 
while len(lst4) >= 2:
    total += rounder(lst4.pop() + lst4.pop())
    
if len(lst4) == 1:  
    total += rounder(lst4.pop())
 
for i in lst0+lst1+lst2:
    total += rounder(i)
    
print(total)
