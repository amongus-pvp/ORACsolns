# https://orac2.info/problem/1193/
Nvotes = int(input())
Rvotes = list(input())

# SOLUTION FROM BIGMANSAM
# i was too lazy to rewrite my C++ soln

A = 0
B = 0
C = 0
for vote in Rvotes:
    if vote == "A":
        A += 1
    elif vote == "B":
        B += 1
    else:
        C += 1
if (A > B > C) or (A > C > B) or (A > B and B == C):
    answer = "A"
elif (B > C > A) or (B > A > C) or (B > C and C == A):
    answer = "B"
elif (C > B > A) or (C > A > B) or (C > B and B == A):
    answer = "C"
else:
    answer = "T"
print(answer)