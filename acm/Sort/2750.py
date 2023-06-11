n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

for i in range(len(numbers)):
    for j in range(len(numbers)-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            
for n in numbers:
    print(n)