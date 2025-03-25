# https://orac2.info/problem/334/
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
 
count = 0
positions = []
 
for i in range(len(arr)):
    if arr[i]%3==0:
        count += 1
        positions.append(i+1)
 
if count != 0:
    print(str(count))
    for i in range(len(positions)):
        print(str(positions[i]))
else:
    print("Nothing here!")
