import string
alphabet = string.ascii_lowercase

action = input('Encode (E) or Decode (D)? ').lower()

def key_prep(key, message):
    key_repetition = ''
    #print(message, len(message))
    #print(key, len(key))
    #Get the number of repetitions the key must have to be the same size as the message
    num_repetition = len(message) / len(key) #Number of repetitions of the full key
    num_char_remaining = len(message) % len(key) #Number of remaining chars 

    #print(num_repetition, num_char_remaining)

    for i in range(int(num_repetition)):
        key_repetition += key

    for i in range(num_char_remaining):
        key_repetition += key[i]

    #print(message, key_repetition)
    return key_repetition

def vigenere_board():
    #print(alphabet)
    board = list()
    for index in range(len(alphabet)):
        #Get a substring from index to the alphabet length + the start of the alphabet until index
        #Ex.: index = 1 -> bcdefghijklmnopqrstuvwxyza + a
        new_alpha = alphabet[index:len(alphabet)] + alphabet[0:index]

        if index == 0: #If index == 0, just use the alphabet
            board.append(alphabet)
        else: #Else, need the alphabet rearranged 
            board.append(new_alpha)
    #print(board)
    return board

def encrypt(message, key, board):
    print(message, key)
    encoded = ''
    for key_char, mess_char in zip(key, message):
        index_key = alphabet.index(key_char)
        index_mess = alphabet.index(mess_char)
        #print(f'{key_char} - {index_key} | {mess_char} - {index_mess}')
        encoded += board[index_key][index_mess]
    print(f'Encoded message:{encoded}')
    return encoded

def decrypt(encrypted, key, board):
    decoded_char = ''
    decoded_message = ''
    for key_char, encryp_char in zip(key, encrypted):
        index_key = alphabet.index(key_char)
        index_mess = alphabet.index(encryp_char)
        decoded_char = board[index_key].index(encryp_char)
        #print(f'{key_char} - {index_key} | {encryp_char} - {index_mess} -> {alphabet[decoded_char]}')
        decoded_message += alphabet[decoded_char]
    print(f'Decoded messsage: {decoded_message}')
    return decoded_message

def menu(action):
    result = ''
    message = input('Whats the message? ').lower()
    key = input('Whats the key? ').lower()
    new_key = key_prep(key, message)
    board = vigenere_board()
    if action == 'd':
        result = decrypt(message, new_key, board)
    else:
        result = encrypt(message, new_key, board)
    
    return result



result = menu(action)
print(result)