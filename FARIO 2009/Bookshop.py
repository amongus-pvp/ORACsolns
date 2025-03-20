# https://orac2.info/problem/169/
x = int(input())
books = [int(input()) for i in range(x)]
dic = {}
c = 1
for i in books:
    dic[i] = c
    c+=1
n = int(input())
books2 = [int(input()) for i in range(n)]
for i in books2:
    print(dic[i])
