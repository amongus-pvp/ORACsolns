# https://orac2.info/problem/1083/
import sys
 
sys.stdin = open("jewelsin.txt", "r")
sys.stdout = open("jewelsout.txt", "w")
 
n = int(input())
s = input()
 
if all(c == 'r' for c in s) or all(c == 'b' for c in s):
    print(n)
    exit()
 
runs = []
current_char = s[0]
count = 1
 
for c in s[1:]:
    if c == current_char:
        count += 1
    else:
        runs.append((current_char, count))
        current_char = c
        count = 1
runs.append((current_char, count))
 
if len(runs) > 1 and runs[0][0] == runs[-1][0]:
    merged_len = runs[0][1] + runs[-1][1]
    runs = [(runs[0][0], merged_len)] + runs[1:-1]
 
if len(runs) == 1:
    print(runs[0][1])
    exit()
 
max_sum = 0
for i in range(len(runs)):
    current_sum = runs[i][1] + runs[(i + 1) % len(runs)][1]
    if current_sum > max_sum:
        max_sum = current_sum
 
print(max_sum)
