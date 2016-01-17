n = int(raw_input())
ar = [int(x) for x in raw_input().strip().split()]
al = sorted(ar)
print(al[n//2])
