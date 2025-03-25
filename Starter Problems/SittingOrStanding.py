# https://orac2.info/problem/330/
r, s = map(int, input().split())
num_tickets = int(input().strip())

num_sitting = min(r*s, num_tickets)
if r*s >= num_tickets:
    num_standing = 0
else:
    num_standing = num_tickets - num_sitting

print(num_sitting, num_standing)
