n = int(raw_input())
a = [int(i) for i in raw_input().strip().split()]
print(" ".join(str(x) for x in sorted(a)))
