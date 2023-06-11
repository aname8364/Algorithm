string = input()
sub_string = input()

arr = []
for c in string:
    arr.append(c)
    if len(arr) >= len(sub_string):
        if ''.join(arr[-len(sub_string):]) == sub_string:
            for i in range(len(sub_string)):
                arr.pop()
                
if not arr:
    print("FRULA")
else:
    print(''.join(arr))