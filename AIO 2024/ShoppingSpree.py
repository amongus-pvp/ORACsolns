N, K = map(int, input().split())
costs = list(map(int, input().split()))
 
for i in range(K):
    answer += costs[i]
 
for j in range(K+1, N-K,2):
    answer += costs[j]
 
print(answer)