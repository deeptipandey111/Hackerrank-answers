for i in range(int(raw_input())):
    c = 0
    l = raw_input()
    lm = len(l)
    for j in range(1,lm):
        if ord(l[j])==ord(l[j-1]):
            c += 1
    print(c)
