# https://orac2.info/problem/203/
n = int(input())  # Total number of daisies
a = int(input())  # Position of the first hippo
b = int(input())  # Position of the second hippo
c = int(input())  # Position of the third hippo
 
# Calculate the gaps
j = a - 1         # Daisies before the first hippo
k = b - a - 1     # Daisies between the first and second hippo
l = c - b - 1     # Daisies between the second and third hippo
m = n - c         # Daisies after the third hippo
 
# Scenario 1: Save daisies on both ends
# Scenario 2: Save daisies on one end and in the largest gap between the hippos
# The final result is the maximum of these two scenarios
print(max(j + m, max(j, m) + max(k, l)))
