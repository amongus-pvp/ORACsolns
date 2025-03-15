# https://orac2.info/problem/301/

nodes, links = map(int, input().split())
transports = {}
 
for n in range(links):
    nums = list(map(int, input().split()))
    if nums[2] not in transports:
        transports[nums[2]] = {} 
    if nums[0] in transports[nums[2]]:
        transports[nums[2]][nums[0]].add(nums[1])
    else:
        transports[nums[2]][nums[0]] = {nums[1],}
        
    if nums[1] in transports[nums[2]]:
        transports[nums[2]][nums[1]].add(nums[0])
    else:
        transports[nums[2]][nums[1]] = {nums[0],}
 
N = int(input())
travel = []
 
for i in range(N):
    travel.append(int(input()))
 
cities = set(range(1, nodes+1))
 
for n in travel:
    newcities = set()
    if not cities:
        break
    if n not in transports:
        cities = set()
        break
    for x in cities:
        if x in transports[n]:
            for a in transports[n][x]:
                newcities.add(a)
    cities = newcities
 
for n in cities:
    print(n)
if not cities:
    print("Impossible")
