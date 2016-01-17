for _ in range(int(raw_input())):
    l1 = list(raw_input().split(" "))
    B,W = int(l1[0]),int(l1[1])
    l2 = list(raw_input().split(" "))
    X,Y,Z = int(l2[0]),int(l2[1]),int(l2[2])
    nt = B*X + W*Y
    lp = X if X<Y else Y
    lc = B if lp== X else W
    mc = W if lp==X else B
    at = (B+W)*lp + mc*Z
    ans = at if at<=nt else nt
    print(ans)
