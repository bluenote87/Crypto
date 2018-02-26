from helpers import alphabet_position, rotate_character

def encrypt(text, rot_key):
    lister = list(rot_key)
    iterate = 0
    rot = 0
    result = ""
    addition = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHA_bet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in text:
        if char in alphabet or char in ALPHA_bet:
            if rot == len(rot_key):
                rot = 0
            iterate = alphabet_position(lister[rot])
            addition = rotate_character(char, iterate)
            result = result + addition
            rot = rot + 1
        else:
            result = result + char
    return result

        


def main():
    message = input("Enter your secret message here: ")
    key = input("Encrypt with: ")
    crypto = encrypt(message, key)
    print(crypto)

if __name__ == "__main__":
    main()