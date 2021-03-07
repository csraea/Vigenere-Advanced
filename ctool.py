# designed by github.com/csraea - All rights reserved. Korotetskyi(c)

import sys

alphabet = " !@#$%^&*()_+-=\\|][\'\":;/.,?><}{0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encrypt(inp, key):
    input_string = inp
    enc_key = key
    enc_string = ""

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position + key_character_position
            if new_position > 93:
                new_position = new_position - 93
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
    return(enc_string)


def decrypt(inp, key):
    input_string = inp
    dec_key = key
    dec_string = ""

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = dec_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position - key_character_position
            if new_position > 93:
                new_position = new_position + 93
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    return(dec_string)

def main():
    # check number of command line arguments
    argnum = len(sys.argv) - 1
    if argnum != 4:
        print("chyba")
        #print("The script is called with %i argument(s)" % (argnum))
        sys.exit()

    # values that are being checked during the argument parsement
    enc = 0
    dec = 0
    password = ""
    pas = 0
    p = 0
    data = ""
    dat = 0

    # check if all arguments are encountered exactly once
    # check whether there are unsupported arguments
    position = 1
    while argnum >= position :
        if str(sys.argv[position]) == "-d":
            dec += 1
        elif str(sys.argv[position]) == "-s":
            enc += 1
        elif str(sys.argv[position]) == "-p":
            p += 1
            position += 1
            password = str(sys.argv[position])
            pas += 1
        else:
            data = str(sys.argv[position])
            dat += 1
        position += 1

    if dec > 1 or enc > 1 or dat > 1 or p > 1 or pas > 1 and ((dec + enc) == 1):
        print("chyba")
        sys.exit()

    # try to open the file & save the contents
    inp = "" 
    try:
        f = open(data, 'r')
    except OSError:
        print("chyba")
        sys.exit()
    with f:
        inp = f.read()

    # The exact encryption / decryption
    if enc :
        print(str(encrypt(inp[::-1], password)))
    else :
        print(str(decrypt(inp, password))[::-1])


if __name__ == "__main__":
    main()