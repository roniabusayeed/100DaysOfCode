alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # Encode only letters from alphabet.
    if char in alphabet:
        position = alphabet.index(char)
        new_position = (position + shift_amount) % len(alphabet)
        end_text += alphabet[new_position]
    else:
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Import and print the logo from art.py when the program starts.
import art
print(art.logo)

end_of_program = False
while not end_of_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Encode/decode input.
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    # Ask user if they want to continute again.
    response = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if response.lower() == "no":
        end_of_program = True

# Let user know the program ended.
print("Goodbye")
