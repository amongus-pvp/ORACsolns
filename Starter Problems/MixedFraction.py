# https://orac2.info/problem/329/
n, d = map(int, input().split())
a = n//d
b = n - (a*d)
if b != 0:
    output_file.write(a, b, d)
else:
    output_file.write(a)
