# https://orac2.info/problem/325/
n, q = map(int, input().split())
answers = []
for i in range(n):
    answers.append(int(input()))
 
for i in range(q):
    print(str(answers[int(input()) - 1]))