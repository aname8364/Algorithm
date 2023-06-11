n = int(input())
word = []

for _ in range(n):
    word.append(input())
    
v = set(word)
print('\n'.join(sorted(v, key=lambda x: (len(x), x))))