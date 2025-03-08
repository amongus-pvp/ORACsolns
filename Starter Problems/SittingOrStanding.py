r, s = map(int, input_line.split())
num_tickets = int(input_file.readline().strip())

if r*s >= num_tickets:
    num_standing = 0
else:
    num_standing = num_tickets - num_sitting

print(num_sitting, num_standing)
