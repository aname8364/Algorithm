n = int(input())

for i in range(1, n+1):
    text = input()
    arr = text.split()
    arr.append(f"Case #{i}:")
    reversed_text = list(reversed(arr))
    print(*reversed_text)

"but not stack"