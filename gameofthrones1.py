string = raw_input()
s = "".join(set(string))
c = 0
found = False
# Write the code to find the required palindrome and then assign the variable 'found' a value of True or False
for i in range(len(s)):
    if(c>1):
        found = False
        pass
    cou = string.count(s[i])
    if(cou%2 !=0):
        c += 1
if c<=1:
    found = True
if not found:
    print("NO")
else:
    print("YES")
