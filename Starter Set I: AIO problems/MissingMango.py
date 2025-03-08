I, C, ID, CD = map(int, input().split())
 
s1, s2 = I + ID, I - ID
s3, s4 = C + CD, C - CD
 
if s1 == s3 or s1 == s4:
    print(s1)
else:
    print(s2)
