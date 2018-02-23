def alphabet_position(letter):
    result = 0
    idx = 0
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    for char in alphabet:
        if letter.lower() == char:
            result = idx
        idx = idx + 1
        
    return result

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHA_bet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = char
    if char in alphabet:
        rotation = alphabet_position(char) + rot
        if rotation < 26:
            result = alphabet[rotation]
        else:
            result = alphabet[rotation % 26]
    if char in ALPHA_bet:
        rotation = alphabet_position(char) + rot
        if rotation < 26:
            result = ALPHA_bet[rotation]
        else:
            result = ALPHA_bet[rotation % 26]
    
    return result



def main():
    print(rotate_character("z", 1))

if __name__ == "__main__":
    main()