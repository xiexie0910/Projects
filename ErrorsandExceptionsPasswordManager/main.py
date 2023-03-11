# ---------------------------- Learning Examples ------------------------------- #
try: # if something in the try block fails then it will go to except
     file = open("a_file.txt")
     a_dictionary={"key":"value"}
     print(a_dictionary['key'])
except FileNotFoundError: # catching an exception
     open("a_file.txt",'w')
except KeyError as error_message: # getting ahold of the error message when you catch an except
     print(f"This key {error_message} does not exist")
else: # else block will execute when all the exceptions are passed
     content = file.read()
     print(content)
finally: # this will run no matter what happens
     raise KeyError("This is an error that I made up") # raising your own errors

# ---------------------------- Implementations ------------------------------- #
     
'''
I have applied this knowledge to improve my previous projects such as:
     PasswordManager on Day 29
     NatoAlphabet List on Day 26
     
'''