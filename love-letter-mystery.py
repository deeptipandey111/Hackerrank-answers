for _ in range(int(raw_input())):
    s = raw_input()
    c = 0
    for i in range(len(s)//2):
        c += abs(ord(s[i])-ord(s[-i-1]))
    print(c)
