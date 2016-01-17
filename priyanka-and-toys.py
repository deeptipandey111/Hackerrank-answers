n = int(raw_input())
a = sorted([int(x) for x in raw_input().split(" ")])
b = [a[0]]
for i in a:
    if i>b[-1]+4:
        b.append(i)
    
print len(b)

#start checking out the last bought item.
