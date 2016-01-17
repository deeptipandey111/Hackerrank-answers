from operator import itemgetter
def give(f,l,g):
    if(g == "M"):
        return("Mr. "+f+" "+l)
    if(g =="F"):
        return("Ms. "+f+" "+l)
n = int(raw_input())
ans = list()
for i in range(n):
    ln = raw_input().split(" ")
    ans.append(ln)
sorted(ans,key=itemgetter(2))
for i in range(n):
    tl = ans[i]
    print(give(tl[0],tl[1],tl[3]))
