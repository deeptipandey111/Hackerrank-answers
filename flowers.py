n, k = list(map(int,raw_input().split()))
a = sorted([int(x) for x in raw_input().split(" ")])
ans = 0
r = 1
while a:
    for j in range(k):
        if a:
            ans += r*a.pop()
    r += 1
print ans

