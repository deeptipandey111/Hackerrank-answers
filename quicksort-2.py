#!/bin/python
def quickSort(ar):   
    if len(ar)<=1:
        return ar
    else:
        left = quickSort([i for i in ar if i<ar[0]])
        right = quickSort([i for i in ar if i>ar[0]])
        ans = list(left + [ar[0]] + right)
        print(" ".join(map(str,left+[ar[0]]+right)))
        return left + [ar[0]] + right

m = input()
ar = [int(i) for i in raw_input().strip().split()]
quickSort(ar)
