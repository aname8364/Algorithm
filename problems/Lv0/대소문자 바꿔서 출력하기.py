str = input()
newstr = ''
for i in str:
    if i.isupper():
        newstr = newstr + i.lower()
    elif i.islower():
        newstr = newstr + i.upper()
print(newstr)