for i in range(int(raw_input())):
    n = int(raw_input())
    a = [int(x) for x in raw_input().strip().split()]
    s2 = sum(x for x in a if x>0)
    s = 0
    #for i in range(n):
     #   if (sum(a[:i+1])) > s:
        #   s = sum(a[:i+1])
    max_ending_here = max_so_far = a[0]
    for x in a[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    s =  max_so_far
    print s,s2
## check why first test case doesn't work
