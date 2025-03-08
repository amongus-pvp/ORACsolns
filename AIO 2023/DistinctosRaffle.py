n, k = map(int, input().strip().split())
tickets = list(map(int, input().strip().split()))
freq = {}
uniq = []
final = []
 
for i in range(n):
    if tickets[i] in freq:
        freq[tickets[i]] += 1
    else:
        freq[tickets[i]] = 1
        uniq.append(tickets[i])
 
for i in range(len(uniq)):
    n = freq[uniq[i]]
    if n == 1:
        final.append(uniq[i])
 
if len(final) != 0:
    print(min(final))
else:
    print(-1)