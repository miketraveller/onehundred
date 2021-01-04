
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(start_text, shift_amount, shift_direction):
    shifted = ""
    if shift_direction == "decode":
            shift_amount *= -1
    for letter in start_text:
        if letter not in alphabet:
            shifted += letter
        else:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            shifted += alphabet[new_position]
    print(f"the {shift_direction}d string is {shifted}")

keep_going = True
while keep_going:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    ceasar(text, shift, direction)

    ans = input("Type yes to continue, no to end: ")
    if ans == 'no':
        keep_going = False