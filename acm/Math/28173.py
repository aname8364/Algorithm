import math

def find_first_multiple(n, x):
    remainder = x % n
    correction = n - remainder if remainder != 0 else 0
    first_multiple = x + correction
    return first_multiple

l, r, b, k = map(int, input().split())

if b>l:
    print(b*k)
else:
    if l%b == 0:
        print(l*k)
    else:
        print(find_first_multiple(b, l)*k)