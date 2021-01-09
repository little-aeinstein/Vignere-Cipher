import math

#this method performs the ciphering procedure
#returned the encrypted message
def encrypted_text(message, key):

    encrypted_message = ''   
    counter = 0

    for message_letter in message:
        key_letter = key[counter]
        key_letter_number = letter_number_mapping[key_letter]
        
        message_letter_number = letter_number_mapping[message_letter]
        ciphertext_number = message_letter_number + key_letter_number

        if(ciphertext_number / 26 > 1):
            ciphertext_number = ciphertext_number % 26

        encrypted_message += number_letter_mapping[ciphertext_number]
        counter += 1
    return encrypted_message

#this method performs the deciphering procedure
#returned the decrypted message
def decrypted_text(message, key):
    
    decrypted_message = ''
    counter = 0

    for message_letter in message:
        key_letter = key[counter]
        key_letter_number = letter_number_mapping[key_letter]

        message_letter_number = letter_number_mapping[message_letter]
        deciphertext_number = message_letter_number - key_letter_number

        if (deciphertext_number <= 0):
            deciphertext_number += 26
        
        decrypted_message += number_letter_mapping[deciphertext_number]
        counter += 1
    return decrypted_message

message = 'send cannon to the hill top'
key = 'BLUE'

#set message and key to uppercase
#remove all spaces in message and key
message = message.upper().replace(' ', '')
key = key.upper().replace(' ', '')

#set the size of the key with the size of the message
size = math.ceil(len(message) / len(key))
key = key * size

#each letter corresponds to a specific number
letters = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A']
numbers = [i for i in range(1, 27)]
letter_number_mapping = dict(zip(letters, numbers))
number_letter_mapping = dict(zip(numbers, letters))

encrypted_message = encrypted_text(message, key)
decrypted_message = decrypted_text(encrypted_message, key)

print(encrypted_message)
print(decrypted_message)