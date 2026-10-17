def vigenere_sq():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    print(f"|   |", end="")
    for letter in alphabet:
        print(f" {letter} |", end="")
    print()

    print("|---|" * (len(alphabet) + 1))

    for i in range(len(alphabet)):
        print(f"| {alphabet[i]} |", end="")

        for j in range(len(alphabet)):
            index = (i + j) % len(alphabet)
            print(f" {alphabet[index]} |", end="")

        print()


vigenere_sq()

def letter_to_index(letter, alphabet):
    return alphabet.index(letter)

def index_to_letter(index, alphabet):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plaintext_index = letter_to_index(plaintext_letter, alphabet)

    cipher_index = (key_index + plaintext_index) % len(alphabet)

    return index_to_letter(cipher_index, alphabet)



def encrypt_vigenere(key, plaintext, alphabet):
    encrypted = ""

    for i in range(len(plaintext)):
        key_letter = key[i % len(key)]
        plaintext_letter = plaintext[i]

        if plaintext_letter in alphabet:
            encrypted_letter = vigenere_index(
                key_letter, plaintext_letter, alphabet
            )
            encrypted += encrypted_letter
        else:
            encrypted += plaintext_letter

    return encrypted


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print(letter_to_index("D", alphabet))
print(index_to_letter(3, alphabet))

print(vigenere_index("K", "H", alphabet))

key = "DAVINCI"
plaintext = "THE EAGLE HAS LANDED"

print(encrypt_vigenere(key, plaintext, alphabet))
