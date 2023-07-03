plain_text = input()

encrypted_text = ""

for char in plain_text:
    ascii_char = ord(char)
    if char.islower():
        ascii_char += 13
        new_char = chr(ascii_char)
        if not new_char.islower():
            ascii_char -= 26
    elif char.isupper():
        ascii_char += 13
        new_char = chr(ascii_char)
        if not new_char.isupper():
            ascii_char -= 26
    encrypted_text += chr(ascii_char)

print(encrypted_text)