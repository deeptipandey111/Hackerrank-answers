n = int(raw_input())
l = list()
for i in range(n):
    l.append(raw_input())
c = 0
ans = list()
charset = "".join(set(l[0]))                 
for j in range(len(charset)):
    ch = charset[j]
    flag = 0
    for i in l:
        if ch in i:
            flag += 1
        if flag==n:
            ans.append(ch)
print(len(ans))    
