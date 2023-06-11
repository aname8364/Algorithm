import sys
input = sys.stdin.readline
num_count = int(input())

numbers = [0 for i in range(10001)]

for i in range(num_count):
    numbers[int(input())] += 1
    
for i in range(len(numbers)):
    while numbers[i] != 0:
        print(i)
        numbers[i] -= 1