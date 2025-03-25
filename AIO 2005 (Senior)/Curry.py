# https://orac2.info/problem/99/
c,r,v = map(int, input().split())
cr=0
rv=0
cv=0
while (c+r>=2 or c+v>=2 or r+v>=2) and (c+r>0 and c+v>0 and r+v>0):
    if c>=v and r>=v and c+r>=2:
        c-=1
        r-=1
        cr+=1
        continue
    if c>=r and v>=r and c+v>=2:
        c-=1
        v-=1
        cv+=1
        continue
    if r>=c and v>=c and r+v>=2:
        r-=1
        v-=1
        rv+=1
        continue
 
print(rv, cv, cr)
