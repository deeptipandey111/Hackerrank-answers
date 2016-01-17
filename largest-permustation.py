n,k = list(map(int,raw_input().split(" ")))
a = [int(x) for x in raw_input().split(" ")]
b = sorted(a)
i = 0
swaps =0
if k>=n-1:
    print " ".join(str(x) for x in b[::-1])
    sys.exit()
else:
    while swaps<k:
        m = a.index(max(a[i:]))
        if a[i] != a[m]:
            a[m],a[i] = a[i],a[m]
            swaps += 1
        i += 1
print " ".join(str(x) for x in a)
