for _ in range(int(raw_input())):
    m = int(raw_input())
    n = int(raw_input())
    a = [int(x) for x in raw_input().strip().split()]
    f = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]+a[j]==m:
                print(" ".join([str(i+1),str(j+1)]))
                f = 1
                break
        if f==1:
            break
