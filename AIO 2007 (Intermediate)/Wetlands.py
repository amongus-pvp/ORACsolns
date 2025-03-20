# https://orac2.info/problem/34/
answer = 0
for i in range(8):
    answer += int(input())
    answer = max(0, answer - 10)
 
print(answer)
