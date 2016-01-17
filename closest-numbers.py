timeout/wrong ans:

n = int(raw_input())
ar = [int(x) for x in raw_input().strip().split()]
m = abs(ar[1]-ar[0])
al = list()
for i in range(0,n-1):
    for j in range(i+1,n):
        if abs(ar[i]-ar[j])<m:
            m = abs(ar[i]-ar[j])
            al = [ar[i],ar[j]]
        elif abs(ar[i]-ar[j])==m:
            al.append(ar[i])
            al.append(ar[j])
#m = min(abs(ar[i-1]-ar[i]) for i in range(1,n))

print(" ".join(str(x) for x in al))


correct one(only in py3)::

#!/usr/bin/env python

import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    array = sorted(map(int, sys.stdin.readline().split()))
    
    min_diff = min(b - a for a, b in zip(array, array[1:]))
    print(*sum(([a, b] for a, b in zip(array, array[1:]) if b - a == min_diff), []))
