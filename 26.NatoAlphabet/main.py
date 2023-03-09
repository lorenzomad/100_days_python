import pandas as pd

def simplify_alphabet(alphabet):
    return alphabet.replace( ",", "").split()


nato_df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_dictionary = {row.letter:row.code for (index, row) in nato_df.iterrows()}

name = input("Input a word:")

phonetic_name = [nato_dictionary[letter.upper()] for letter in name]

print(phonetic_name)