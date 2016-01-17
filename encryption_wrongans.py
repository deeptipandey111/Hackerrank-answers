import math 
s = raw_input().strip()
L = len(s)
r = int(math.floor(math.sqrt(L)))
c = int(math.ceil(math.sqrt(L)))
#print(r,c)
h = 0
ans = ""
for i in range(c):
    w = ""
    for j in range(r):
        if (i+j*c)<L:
            w =  w+s[i+j*c]
        else:
            h = h+1
    w = w+" "
    ans = ans+w
print(ans)
