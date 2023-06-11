n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

posStack = []
currentNum = 1
result = []

for number in numbers:
    if number >= currentNum:
        for i in range(currentNum, number+1):
            posStack.append(i)
            result.append("+")
            if i == number:
                posStack.pop()
                result.append("-")
        currentNum = number+1
    else:
        if posStack and number == posStack[-1]:
            posStack.pop()
            result.append("-")
        else:
            result = ["NO"]
            break

print("\n".join(result))