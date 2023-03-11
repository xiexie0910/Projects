############### Guess The Number Project #####################


logo = '''

  ________                              ___________.__              _______               ___.                 
 /  _____/ __ __   ____   ______ ______ \__    ___/|  |__   ____    \      \  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/   |    |   |  |  \_/ __ \   /   |   \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \    |    |   |   Y  \  ___/  /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  >   |____|   |___|  /\___  > \____|__  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/                  \/     \/          \/            \/    \/     \/       

'''

import random
print(logo)

def guess_the_number(mode):
     '''
     This function randomly generates a number and gets the user to guess it
     
     ----------
     parameters
     ----------
     
     mode:     The mode that the user wants to play in (easy/hard)
     
     -------
     outputs
     -------
     
     It will tell the user the result of their guesses
     '''
     
     # sets the number of attempts based on the mode using if statements
     if mode == 'easy':
          attempt = 10
     else:
          attempt = 5

     # using while loop to loop through all the conditions while the user still has attempts
     while attempt != 0:
          # tells the user how many attempts left
          print(f"You have {attempt} attempts to make a guess")
          # asks them to make a guess
          guess = int(input("I'm thinking of a number between 1 to 100\nMake a guess: "))
          # using if statements to check through all the conditions and prints corresponding responses
          if randnum == guess:
               print(f"You got it! The answer was {guess}")
               break
          elif guess > randnum:
               print("####### Too high #######")
               attempt -=1
          else:
               print("####### Too low #######")
               attempt -=1
     # reveals the answer if the player has no more attempts left
     if attempt == 0:
          print(f"You failed. The answer was {randnum}")
# asks the user for the mode they want to play in
mode = input("Welcome to Guess The Number Game!!!\nDo you want to play the 'easy' or 'hard' mode: ").lower()
# randomly generate a number 
randnum = random.randint(1,100)
# call guess the number function
guess_the_number(mode)


