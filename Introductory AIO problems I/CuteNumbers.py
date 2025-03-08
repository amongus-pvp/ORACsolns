d = int(input())
arr = []
for i in range(d):
    x = int(input())
    arr.append(x)
print(arr)
 
length = len(arr)
cuteness = 0
for i in range(length):
    if arr[length-i-1] == 0:
        cuteness += 1
    else:
        break
 
print(cuteness)