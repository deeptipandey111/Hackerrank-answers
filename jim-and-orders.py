import operator
d = {}
for i in range(int(raw_input())):
    l = raw_input().split(" ")
    d[i+1] = int(l[0]) + int(l[1])
    
sd = sorted(d.items(),key = operator.itemgetter(1))
l1 = []
#print sd
s = ""
for (key, value) in sd:
    s = s+ str(key) + " "
#print " ".join(str(x) for x in l1)
#print l1
print s
