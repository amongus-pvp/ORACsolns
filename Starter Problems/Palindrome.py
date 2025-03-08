n = int(input())

s = list(input())

left = 0
right = n - 1

# we'll js inch these 2 pointers towards each other until one of them doesnt match and then boom shakalaka

while left < right:
  if s[left] != s[right]:
    if s[left] > s[right]: # left pointer is lower in alphabetical order 'a' < 'b'
      s[left] = s[right]
    else:
      s[right] = s[left]
  left += 1
  right -= 1

print(''.join(s))
