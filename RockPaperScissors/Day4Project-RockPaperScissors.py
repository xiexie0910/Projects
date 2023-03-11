# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1

import random 
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock,paper,scissors]

randnum = random.randint(0,2)
num = int(input("Please enter 0 for rock, 1 for paper or 2 for scissors: "))

if num >= 3 or num < 0:
    print("You typed an invalid number")
elif num == randnum:
    print(choices[num])
    print(f"Computer chose:\n{choices[randnum]}")
    print("It's a tie")
elif (num == 0 and randnum == 1) or (num == 1 and randnum == 2) or (num == 2 and randnum == 0):
    print(choices[num])
    print(f"Computer chose:\n{choices[randnum]}")
    print("You lose")
elif (num == 0 and randnum == 2) or (num == 1 and randnum == 0) or (num == 2 and randnum == 1):
    print(choices[num])
    print(f"Computer chose:\n{choices[randnum]}")
    print("You won")



