'''
copyright (c) 2017. Cody-Joe Abe. All rights reserved

'''
import sys
import os

def decoder(message, offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""
    message = message.lower()
    for i in range(len(message)):
        alphabet_index = alphabet.index(message[i])
        if (message[i] == " "):
            decoded_message = decoded_message + " "
        if (alphabet_index + offset > 25):
            new_offset = (offset + alphabet_index) % 26
            new_letter = alphabet[new_offset]
            decoded_message = decoded_message + new_letter
        else:
            new_letter = alphabet[offset + alphabet_index]
            decoded_message = decoded_message + new_letter
    return decoded_message




def main(argv):
    print(decoder("XVATBSZVKRQFNYNQF", 13))

if __name__ == "__main__":
    main(sys.argv[1:])
