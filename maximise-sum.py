for i in range(int(raw_input())):
    lin = raw_input().split()
    n,m = int(lin[0]),int(lin[1])
    a = [int(x) for x in raw_input().strip().split()]
    ma = 0
    for i in range(n):
        s = sum(a[j] for j in range(i+1))
        #print s
        if s%m > ma:
            ma = s%m
    print(ma)
