n = int(raw_input())
inp = list()
for i in range(n):
    lin = raw_input().split(" ")
    inp.append(int(lin[0]))
ans = list()
for j in range(100):
    ans.append(sum(x<=j for x in inp))
print(" ".join(str(x) for x in ans))
