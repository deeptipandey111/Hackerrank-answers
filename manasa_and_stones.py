for _ in range(int(raw_input())):
    n,d1,d2 = int(raw_input()), int(raw_input()), int(raw_input())
    n = n-1
    l = list()
    l.append(n*d1)
    l.append(n*d2)
    for i in range(1,n):
        l.append(i*d1 + (n-i)*d2)
    l = sorted(l)
    #ans = " ".join(str(l)).strip('[]')
    print ' '.join(str(x) for x in l)
    #print(sorted(l))
    
