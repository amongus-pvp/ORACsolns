N, K = map(int, input().split())
 
for i in range(0, N):
    S.append(int(input()))
 
sections = [[], [], []]
 
for i in range(0, N):
    sections[i%3].append(S[i])
 
def calculate_mode(a):
    count = [0 for x in range(K+1)]
    for note in a:
        count[note] += 1
    return max(count)
 
kept_the_same = 0
kept_the_same += calculate_mode(sections[0])
kept_the_same += calculate_mode(sections[1])
kept_the_same += calculate_mode(sections[2])
 
answer = N - kept_the_same
print(answer) # basically js calculate the mode