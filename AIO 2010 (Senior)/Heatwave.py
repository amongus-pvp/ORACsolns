# https://orac2.info/problem/226/
def longest_heatwave(N, H, temperatures):
    current_length = 0
    max_length = 0
 
    for temp in temperatures:
        if temp >= H:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0
 
    return max_length
 
N, H = map(int, input().split())
temperatures = [int(input()) for _ in range(N)]
 
# Compute the result
result = longest_heatwave(N, H, temperatures)
 
print(result)
