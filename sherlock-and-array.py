for _ in range(int(raw_input())):
    n = int(raw_input())
    f = 0
    ar = [int(x) for x in raw_input().strip().split()]
    for i in range(n):
        left = sum(ar[j] for j in range(i))
        right = sum(ar[j] for j in range(i+1,n) if i+1<n)
        if left == right:
            print("YES")
            f = 1
            break
    if f==0:
        print("NO")

this failed two test cases to timeout....

correct ans::
import sys


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    
    for _ in range(T):
        N = int(sys.stdin.readline())
        A = list(map(int, sys.stdin.readline().split()))

        if N == 1:
            print('YES')
        elif N == 2:
            print('NO')
        else:
            L, R = 0, sum(A[1:])

            for i in range(1, N - 1):
                L, R = L + A[i - 1], R - A[i]

                if L == R:
                    print('YES')
                    break
            else:
                print('NO')
