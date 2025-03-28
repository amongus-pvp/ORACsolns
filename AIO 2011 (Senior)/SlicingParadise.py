# https://orac2.info/problem/162/
N = int(input())
resort_list = [None for i in range(N)]
forest_list = [1 for i in range(N)]
num_of_park = 1
 
answer = 1
 
for i in range(N):
    num = int(input())
    resort_list[num - 1] = i
 
for item in resort_list:
    forest_list[item] = 0
    
    if item - 1 >= 0 and forest_list[item - 1] == 1:
        l = True
    else:
        l = False
    
    if item + 1 < N and forest_list[item + 1] == 1:
        r = True
    else:
        r = False
    
    if l and r:
        num_of_park += 1
    elif (not l) and (not r):
        num_of_park -= 1
        
    answer = max(answer, num_of_park)
    
print(answer)
