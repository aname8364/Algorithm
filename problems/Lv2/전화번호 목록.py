def solution(phone_book):
    hash_set = set(phone_book)
    for phone in phone_book:
        for i in range(1, len(phone)):
            if phone[:i] in hash_set:
                return False
    return True