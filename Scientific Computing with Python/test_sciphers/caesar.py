import string

def caesar(message, skips, decrypt=False):
    if decrypt:
        skips = skips * -1
    final_message = ''
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            index = alphabet.index(char)
            print(char, index, index + skips, alphabet[(index + skips) % len(alphabet)])
            final_message += alphabet[(index + skips) % len(alphabet)]
    return final_message

message = input('Message being encoded:')
skips = int(input('Number of skips:'))
alphabet = string.ascii_lowercase

encoded = caesar(message, skips)
print('Encoded: ', encoded)

decoded = caesar(encoded, skips, True)
print('Decoded: ', decoded)
