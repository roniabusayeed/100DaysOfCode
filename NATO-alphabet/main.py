import pandas

alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
while True:
    try:
        word = input("Enter a word: ").upper()
        codes = [alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break

print(codes)
