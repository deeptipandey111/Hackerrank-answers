import collections
if __name__ == '__main__':
    A = raw_input()
    B = raw_input()
    
    a = collections.Counter(A)
    b = collections.Counter(B)
    
    length = sum(min(a[c], b[c]) for c in (set(A) & set(B)))
    print(len(A) +len(B) - 2*length)
