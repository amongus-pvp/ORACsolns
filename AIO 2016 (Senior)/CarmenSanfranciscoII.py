# https://orac2.info/problem/8/
import sys
 
sys.setrecursionlimit(1000000000)
# Get input.
N, C = map(int, input().split())
bank_list = list(map(int, input().split()))
 
if N == 1:
    print(1)
 
time_list = list(map(int, input().split()))

answer = 0
 
bank_range = bank_list[-1] - bank_list[0]
left_margin_list = [None for i in range(bank_range)]
right_margin_list = [None for i in range(bank_range)]
for i in range(bank_range):
    left_margin_list[i] = time_list[i + bank_list[0] - 1] - (i + 1)
    right_margin_list[i] = time_list[bank_list[-1] - 2 - i] - (i + 1)
 
if C == 1:
    left_bank_possible_range = N
    right_bank_possible_range = N
else:
    left_bank_possible_range = min(left_margin_list) if left_margin_list else -1
    right_bank_possible_range = min(right_margin_list) if right_margin_list else -1
 
to_left_range = None
to_right_range = None
 
def update_range(ran, left, right):
    pass
 
if left_bank_possible_range >= 0:
    to_left_range = [bank_list[0], bank_list[0]]
    # left of left bank range
    margin = 1000000
    for i in range(left_bank_possible_range):
        time_list_idx = bank_list[0] - 2 - i
        if time_list_idx < 0:
            break
        margin = min(margin, time_list[time_list_idx]) - 1
        if margin < 0:
            break
        to_left_range[0] -= 1
    # right of left bank range
    margin = 1000000
    for i in range(left_bank_possible_range):
        time_list_idx = bank_list[0] - 1 + i
        if time_list_idx > N - 2:
            break
        margin = min(margin, time_list[time_list_idx]) - 1
        if margin < 0:
            break
        to_left_range[1] += 1
    
if right_bank_possible_range >= 0:
    to_right_range = [bank_list[-1], bank_list[-1]]
    # left of right bank range
    margin = 1000000
    for i in range(right_bank_possible_range):
        time_list_idx = bank_list[-1] - 2 - i
        if time_list_idx < 0:
            break
        margin = min(margin, time_list[time_list_idx]) - 1
        if margin < 0:
            break
        to_right_range[0] -= 1
    # right of right bank range
    margin = 1000000
    for i in range(right_bank_possible_range):
        time_list_idx = bank_list[-1] - 1 + i
        if time_list_idx > N - 2:
            break
        margin = min(margin, time_list[time_list_idx]) - 1
        if margin < 0:
            break
        to_right_range[1] += 1
 
 
 
# Combine to_left_range and to_right_range
answer_set = set()
if to_left_range:
    answer_set.update(set(range(to_left_range[0], to_left_range[1] + 1)))
if to_right_range:
    answer_set.update(set(range(to_right_range[0], to_right_range[1] + 1)))
 
answer = len(answer_set)
print(answer)
