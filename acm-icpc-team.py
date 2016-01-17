line = raw_input().split(" ")
n = int(line[0])
m = int(line[1])
#n = int(raw_input())
bl = list()
for _ in range(n):
    bl.append(int(raw_input(),2))
ol = list()
for i in range(n-1):
    for j in range(i+1,n):
        ol.append(bin(bl[i]|bl[j]).count('1'))

print(max(ol))
print(ol.count(max(ol)))
