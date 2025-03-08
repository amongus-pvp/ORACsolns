def cScore(word):
    score = 0
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            score += 1
    return score

N = int(input())
word = input()
 
for i in range(len(word)):
    if word[i] == "?":
        x = i
        break
if x == 0:
    word = word[1] + word[1:]
elif x == N-1:
    word = word[:-1] + word[-2]
else:
    sword = word[x-1:x+2]
    word1 = list(sword)
    word2 = list(sword)
 
    word1[1] = word1[0]
    word2[1] = word2[2]
 
    word1, word2 = "".join(word1), "".join(word2)
 
    word = list(word)
 
    if cScore(word1) > cScore(word2):
        word[x] = word1[1]
    elif cScore(word2) >= cScore(word1):
        word[x] = word2[1]
 
    word = "".join(word)

print(cScore(word))