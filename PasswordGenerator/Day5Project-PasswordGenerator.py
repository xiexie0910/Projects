# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# randomly generate input rather than through user input
nr_letters = random.randint(0,len(letters)-1)
nr_symbols = random.randint(0,len(symbols)-1)
nr_numbers = random.randint(0,len(numbers)-1)

# generating the random letters, symbols and numbers ### the reason why random.randint(0,len(letters)-1) cannot be replaced by nr_letters is because they do not co exist
password_letter = [(letters[random.randint(0,len(letters)-1)]) for _ in range(1, nr_letters)]
password_symbol=[symbols[random.randint(0,len(symbols)-1)] for _ in range(1, nr_symbols)]
password_number=[numbers[random.randint(0,len(numbers)-1)] for _ in range(1, nr_numbers)]

password = list(password_letter + password_symbol + password_number)
# randomly shuffling the string 
random.shuffle(password)
result = ''.join(password)
print(f"Your password is: {result}")
