import string
alphabet = string.ascii_lowercase

backwards_alphabet = alphabet[::-1]

print(alphabet)
print(backwards_alphabet)

message = input('Whats the messege? ')

def encrypt(message):
    encoded = ''
    for letter in message:
        index_alpha = alphabet.index(letter)
        letter_encoded = backwards_alphabet[index_alpha]
        encoded += letter_encoded
    return encoded

def decrypt(message):
    decoded = ''
    for letter in message:
        index_encoded = backwards_alphabet.index(letter)
        letter_decoded = alphabet[index_encoded]
        decoded += letter_decoded
    return decoded

encoded = encrypt(message)
decoded = decrypt(encoded)
print(encoded, decoded)