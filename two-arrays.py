for _ in range(int(raw_input())):
    l = raw_input().split(" ")
    n = int(l[0])
    k = int(l[1])
    f = 0
    a = sorted([int(x) for x in raw_input().split(" ")])
    
    b = sorted([int(x) for x in raw_input().split(" ")])
    b = b[::-1]
    
    for i in range(n):
        if a[i]+b[i] < k:
            print("NO")
            f = 1
            break
    else:
        print("YES")


#in this, I wasnt handling cases when the sum becomes > k. hence the errors!! take care next time!!
