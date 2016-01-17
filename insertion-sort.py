def insertionSort(ar): 
    n = len(ar)
    for i in range(1,n):
        if ar[n-i-1]>v:
            ar[n-i] = ar[n-i-1]
            print ' '.join(str(x) for x in ar)
        else:
            ar[n-i] = v
            print ' '.join(str(x) for x in ar)
            break
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
v = ar[len(ar)-1]
insertionSort(ar)

