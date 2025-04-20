# https://orac2.info/problem/116/
N = int(input())
d = set()

for i in range(N):
    word = input()
    d.add(word)

M = int(input())
for _ in range(M):
    word = input()
    if word in d:
        print(word) # we dont have to change the word
        continue
    # chr(97) is a
    # chr(122) is z
    flag = False
    for i in range(len(word)):
        temp = list(word[:]) # dont want some freaky reference stuff to happen
        for j in range(97, 123):
            temp[i] = chr(j)
            if "".join(temp) in d:
                print("".join(temp))
                flag = True
                break # move onto next testcase
        if flag:
            break

    if not flag:
        print("?") # couldnt find word
