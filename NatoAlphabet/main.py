### nato list ###

# import pandas module
import pandas as pd 
# read csv
data = pd.read_csv('nato_phonetic_alphabet.csv')
# using dictionary comprehension to create a dictionary
nato_list = {row.letter:row.code for (index,row) in data.iterrows()} # iterrows() helps us access the pandas dataframe like accessing a list


def generate_phonetic():
     # user inputs a word of their choice
     user_input = input("Please enter a word: ").upper()
     try:
          # storing the nato alphabet into a list by accessing the equivalent letter in the nato dictionary
          final_word = [nato_list[letter] for letter in user_input]
          
     except KeyError:
          print("Please enter letters from the alphabet")
          generate_phonetic()
     else:
          print(final_word)

generate_phonetic()