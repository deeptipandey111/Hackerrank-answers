n = int(raw_input())
a = [int(i) for i in raw_input().strip().split()]
#print(a)
ans = list()
for k in range(int(100)):
    ans.append(a.count(k))
    #print(a.count(1))
print(" ".join(str(x) for x in ans))
