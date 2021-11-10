alphabet = "abcdefghijklmnopqrstuvwxyz"

from_alphabet_to_num = dict(zip(alphabet,range(len(alphabet))))
from_num_to_alphabet = dict(zip(range(len(alphabet)),alphabet))
 

def encode(message,key):
    for character in message:
        if character not in alphabet:
            message = message.replace(character,"")
    code = ""
    split_message = [message[i:i + len(key)] for i in range(0,len(message),len(key))]

    for message in split_message:
        i = 0
        for character in message:
            number = (from_alphabet_to_num[character] + from_alphabet_to_num[key[i]]) % len(alphabet)
            code += from_num_to_alphabet[number]
            i +=1

    return code

def decode(code,key):
    message = ""
    for character in code:
        if character not in alphabet:
            code = code.replace(character,"")
    split_code = [code[i:i + len(key)] for i in range(0,len(code),len(key))]

    for code in split_code:
        i = 0
        for character in code:
            number = (from_alphabet_to_num[character] - from_alphabet_to_num[key[i]]) % len(alphabet)
            message += from_num_to_alphabet[number]
            i+=1
    return message

def encode2(message,key):
    code = ""
    for character in message:
        if character not in alphabet:
            message = message.replace(character,"")
    key2 = key[0] + message[:len(message)-1]
    i = 0
    for character in message:
        number = (from_alphabet_to_num[character] + from_alphabet_to_num[key2[i]]) % len(alphabet)
        code += from_num_to_alphabet[number]
        i +=1
    return code

def decode2(code,key):
    message = ""
    for character in code:
        if character not in alphabet:
            code = code.replace(character,"")
    key2 = key[0] + code[:len(code)-1]
    i = 0
    for character in code:
        number = (from_alphabet_to_num[character] - from_alphabet_to_num[key2[i]]) % len(alphabet)
        message += from_num_to_alphabet[number]
        i+=1
    return message

def encode3(message,key):
    code = ""
    for character in message:
        if character not in alphabet:
            message = message.replace(character,"")
    i = 0
    key2 = key[0]
    for character in message:
        number = (from_alphabet_to_num[character] + from_alphabet_to_num[key2[i]]) % len(alphabet)
        code += from_num_to_alphabet[number]
        key2 += from_num_to_alphabet[number]
        i +=1
    return code

def decode3(code,key):
    message = ""
    for character in code:
        if character not in alphabet:
            message = message.replace(character,"")
    i = 0
    key2 = key[0] + code[:len(code)-1]
    for character in code:
        number = (from_alphabet_to_num[character] - from_alphabet_to_num[key2[i]]) % len(alphabet)
        message += from_num_to_alphabet[number]
        i +=1
    return message



