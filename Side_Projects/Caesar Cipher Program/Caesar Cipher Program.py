from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
            'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
            'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                new_position = position + shift_amount
            elif cipher_direction == "decode":
                new_position = position - shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

#Main Program
print(logo)
program_on = True

while program_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower()
    if should_continue == 'yes':
        pass
    elif should_continue == 'no':
        program_on = False