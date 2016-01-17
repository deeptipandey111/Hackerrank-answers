def partition(ar):  
    ans = list()
    p = ar[0]
    les = list()
    ans.append(p)
    for i in range(1,len(ar)):
        if(ar[i]>p):
            ans.append(ar[i])
        if(ar[i]<p):
            ans = [ar[i]] + ans
    print(" ".join(str(x) for x in ans))
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
partition(ar)
