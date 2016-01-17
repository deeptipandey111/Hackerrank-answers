n = input()
k = input()-1
a = sorted([input() for _ in range(0,n)])
l = []
i = 0
while i+k<n:
    mi = a[i]
    ma = a[i+k]
    i += 1
    l.append(ma-mi)
print min(l)
