card_count, number = map(int, input().split())
cards = list(map(int, input().split()))

high_number = 0

for i in range(card_count):
    for j in range(i+1, card_count):
        for k in range(j+1, card_count):
            n = cards[i] + cards[j] + cards[k]
            if n > high_number and not n > number:
                high_number = n
print(high_number)