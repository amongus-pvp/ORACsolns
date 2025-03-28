# https://orac2.info/problem/48/
N, K = map(int, input().split())
 
pos_list = [0 for i in range(N)]
keep_first_shift_list = [0 for i in range(N)]
abs_shift_list = [None for i in range(N)]
 
for i in range(1, N):
    d = int(input())
    pos_list[i] = pos_list[i - 1] + d
    keep_first_shift_list[i] = i * K - pos_list[i]

whole_shift = median(keep_first_shift_list)
for i in range(N):
    abs_shift_list[i] = abs(keep_first_shift_list[i] - whole_shift)
    
answer = int(sum(abs_shift_list))

print(answer)
