N = int(input())
 
A = list(map(int, input().split()))
B = list(map(int, input().split()))
 
ans = 0
ps = 0
list = [0]
 
for i in range(N-1):
    ps += A[i] - B[i]
    list += [ps]
 
list.sort()
med = list[len(list)//2]
for v in list:
    ans += abs(v-med)

print(ans)

# hard ahh problem