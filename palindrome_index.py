for i in range(int(raw_input())):
    s = raw_input()
    if s==s[::-1]:
        print("-1")
    else:
        for i in range(len(s)//2):
            if s[i]!= s[-i-1]:
                x = s[:i] + s[i+1:]
                print(i if x==x[::-1] else len(s)-i-1)
                break
        else:
            print("0")
    
