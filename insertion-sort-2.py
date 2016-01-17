def insertionSort(ar):    
    for i in range(1,len(ar)):
        for j in range(0,i):
            if ar[i]<ar[j]:
                ar[i],ar[j] = ar[j],ar[i]
        print " ".join(str(x) for x in ar)
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
