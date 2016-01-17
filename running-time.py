def insertionSort(ar):  
    c = 0
    for i in range(1,len(ar)):
        for j in range(0,i):
            if ar[i]<ar[j]:
                c += 1
                ar[i],ar[j] = ar[j],ar[i]
    print(c)
    return ""

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
