alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
def user_input():
    # asks the user for the following input
    direction = str(input("Type 'encode' to encrypt, type 'decode' to decrypt:\n"))
    text = input("Type your message:\n").lower()
    # 26 accounts for any shift number that is greater than the lenght of the alphabet
    shift = int(input("Type the shift number:\n")) % 26
    
    return direction, text, shift

def encrypt(text, shift):
    '''
    This function takes an input string and a shift number and shifts each letter in the string by the given shift number
    
    ----------
    Parameters
    ----------
    
    text:   this is a string that contains the message that the user wants to encrypt
    shift:  this is the number that the user wish to shift each letter by
    
    -------
    Outputs
    -------
    
    A message that displays the encrypted text
    '''
    # converts the text into a list 
    text=list(text)
    # using a for loop to shift every letter in the list by the given shift number
    for i in range(0,len(text)):
        if text[i] in alphabet: 
            index = alphabet.index(text[i])
            # shifting the number back to the start of the alphabet based on the condition
            if index >= len(alphabet)-shift:
                text[i] = alphabet[index+shift-26]
            else:
                text[i] = alphabet[index+shift]
    print(f"the encoded text is {''.join(text)}")

def decrypt(text,shift):
    '''
    This function takes an input string and a shift number and shifts each letter in the string by the given shift number
    
    ----------
    Parameters
    ----------
    
    text:   this is a string that contains the message that the user wants to decrypt
    shift:  this is the number that the user wish to shift each letter by
    
    -------
    Outputs
    -------
    
    A message that displays the decrypted text
    '''
    # converts text into a list
    text=list(text) 
    # using a for loop to shift every letter in the text
    for i in range(0,len(text)):
        if text[i] in alphabet:
            index = alphabet.index(text[i])
            # using if conditions to account for letters at the front of the alphabet like 'a'
            if index < shift:
                text[i] = alphabet[index-shift+26]
            else:
                text[i] = alphabet[index-shift]
    # join and prints the decoded text
    print(f"the decoded text is {''.join(text)}")

def caesar(direction,text,shift):
    '''
    This function takes a direction, an input string and a shift number and shifts each letter in the string by the given shift number
    
    ----------
    Parameters
    ----------
    
    direction: this is a string that tells us if the user wants to decrypt or encrypt the input string
    text:      this is a string that contains the message that the user wants to decrypt
    shift:     this is the number that the user wish to shift each letter by
    
    -------
    Outputs
    -------
    
    A message that displays the decrypted text
    '''
    if direction == 'encode':
        encrypt(text,shift)
    elif direction == 'decode':
        decrypt(text,shift)
    else:
        print("Please enter a correct message")

# prints logo
print(logo)
# asks for user input
direction,text,shift = user_input()
# calls the caesar function to execute the user's intended command
caesar(direction,text,shift)
# asks the user if they want to execute the same command with another message
repeat = input("Would you like to encrypt or decrypt another message? (yes/no): ").lower()
# using a while loop to keep asking for user input as long as the user says yes
while repeat == 'yes':
    direction,text,shift = user_input()
    caesar(direction,text,shift)
    repeat = input("Would you like to encrypt or decrypt another message? (yes/no): ").lower()

print("\nGoodbye")


