from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    result = ""
    addition = ""
    for char in text:
        addition = rotate_character(char, rot)
        result = result + addition
    return result


def main():
    message = input("Enter your secret message here: ")
    key = int(input("Rotate by: "))
    crypto = encrypt(message, key)
    print(crypto)

if __name__ == "__main__":
    main()