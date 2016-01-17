lo, up = int(raw_input()), int(raw_input())
ans = list()
for n in range(lo,up):
    if n<1:
        break
    sq = str(n**2)
    if sq=='1':
        ans.append(1)
        continue
    f = int(sq[:-len(str(n))]) if len(sq)>1 else 0      ##this turned out to be super important,the else 0 part,coz leading 0's
    s = int(sq[-len(str(n)):])
    if f+s==n:
        ans.append(n)
if not ans:
    print("INVALID RANGE")
else:
    print ' '.join(str(x) for x in ans)
