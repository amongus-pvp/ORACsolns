# https://orac2.info/problem/62/
import sys
 
sys.setrecursionlimit(1000000000)
 
T = int(input())
col_dict = {}
 
answer = 0
 
for i in range(T):
    x, y = map(int, input().split())
    if x in col_dict:
        col_dict[x][0] = min(col_dict[x][0], y)
        col_dict[x][1] = max(col_dict[x][1], y)
    else:
        col_dict[x] = [y, y, None]
 
col_list = sorted(col_dict.items())
for item in col_list:
    min_y = item[1][0]
    max_y = item[1][1]
    # diff_y
    item[1][2] = max_y - min_y
 
min_x = col_list[0][0]
max_x = col_list[-1][0]
# The whole span of all columns in x
x_span = max_x - min_x
 
# Sum of all columns
sum_col = sum((item[1][2] for item in col_list))
 
# list of each column ends
ends_list = [(item[1][0], item[1][1]) for item in col_list]
 
len_ends_list = len(ends_list)
if len_ends_list == 1:
    answer = sum_col
else:
    # min sum starting from head
    last_head_min_sum = 0
    # min sum starting from tail
    last_tail_min_sum = 0
    
    for i in range(1, len_ends_list):
        head_head = abs(ends_list[i][0] - ends_list[i - 1][0])
        tail_head = abs(ends_list[i][0] - ends_list[i - 1][1])
        head_tail = abs(ends_list[i][1] - ends_list[i - 1][0])
        tail_tail = abs(ends_list[i][1] - ends_list[i - 1][1])
        
        head_min_sum = min(last_head_min_sum + head_tail, last_tail_min_sum + tail_tail)
        tail_min_sum = min(last_head_min_sum + head_head, last_tail_min_sum + tail_head)
        
        last_head_min_sum = head_min_sum
        last_tail_min_sum = tail_min_sum
    
    sum_min_row_diff = min(head_min_sum, tail_min_sum)
    answer = x_span + sum_col + sum_min_row_diff
 
print(answer)
