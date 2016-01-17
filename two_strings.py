for i in range(int(raw_input())):
    flag = 0
    f = ''.join(set(raw_input()))
    s = ''.join(set(raw_input()))
    for ch in f:
        if ch in s:
            flag = 1
            break
        else:
            continue
    if flag == 1:
        print("YES")
    else:
        print("NO")
    
