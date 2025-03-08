d, w = map(int, input().split())
dictionary = {} # I to W
 
for i in range(d):
    I, W = map(int, input().split())
    dictionary[I] = W
 
for i in range(w):
    curline = int(input())
    if curline in dictionary:
        print(str(dictionary[curline]))
    else:
        print("C?")
