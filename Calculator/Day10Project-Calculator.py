# imports the modules for clearing the console
from replit import clear

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

# defined a function that asks the user for all the inputs
def user_input():
     '''
     This function asks the user for all the inputs required to carry out the following operations
     
     ----------
     parameters
     ----------
     
     num1:          this is the first number that the user enters
     operationtype: this is the operation that the user wants to perform
     num2:          this is the second number that the user enters
     
     -------
     outputs
     -------
     
     num1:          this is the first number that the user enters
     operationtype: this is the operation that the user wants to perform
     num2:          this is the second number that the user enters
     
     '''
     # asks the user for the first and second number as well as the operation type
     num1 = float(input("Please enter the first number: "))
     operationtype = input("Please choose an operation: + - * / ^ ")
     num2 = float(input("Please enter the next number: "))
     return num1, operationtype, num2

def calculation(num1,num2):
     '''
     this function performs either addition,subtraction,multiplication,division, or exponential action to the 2 numbers given by the user
     
     ----------
     parameters
     ----------
     
     num1:     this is the first number that the user entered
     num2:     this is the second number that the user entered
     
     -------
     outputs
     -------
     
     returns the result of the selected operation     
     '''
     
     # using if statements to check the operation type and return the result of the selected operation
     if operationtype == '+':
          return num1 + num2
     elif operationtype == '-':
          return num1-num2
     elif operationtype == '*':
          return num1*num2
     elif operationtype == '/':
          return num1/num2
     elif operationtype == '^':
          return num1**num2

def check_operationtype(operationtype):
     '''
     this function checks if the operation type is valid and returns true if valid, false otherwise
     
     ----------
     parameters
     ----------
     
     operationtype:      this is the operation type inputted by the user
     
     -------
     outputs
     -------
     
     returns a binary variable that validates the validity of the operation type   
     '''
     # using if statements to check if the operation type is valid
     if operationtype != '+' and operationtype != '-' and operationtype != '*' and operationtype != '/' and operationtype != '^':
          return False
     else:
          return True

     
#initialising an empty answers list
answers = []
# getting user input
num1, operationtype, num2 = user_input()

# using if statements to call the check_operationtype function and check if the operation type is valid
if not check_operationtype(operationtype):
     print("Calulation terminated")
else:
     # appends the first result to the answer list
     answers.append(calculation(num1,num2))
     # printing the result in a set format
     print(f"{num1} {operationtype} {num2} = {calculation(num1,num2)}")
     # asks user for further command
     playon = input("Do you wish to perform more calculations? (yes/no) ").lower()
     # using while loop to continue the calculation if the user wants to do more calculations
     while playon == "yes":
          # ask the user which mathematical operation that will be performed
          continueplay = input("Do you wish to continue calculating from the current result (c),\nor start a new calculation (n),\nor terminate calculation (t)? (c/n/t) ").lower()
          # using if statement to execute the required operation
          if continueplay == 'c':
               print(f"The first number is {answers[len(answers)-1]}")
               # ask the user which mathematical operation that will be performed
               operationtype = input("Please choose an operation: + - * / ^ ")
               # if the operation type is valid then execute the required operation
               if check_operationtype(operationtype):
                    # asks the user for the second number
                    num2 = float(input("Please enter the next number: "))
                    print(f"{answers[len(answers)-1]} {operationtype} {num2} = {calculation(answers[len(answers)-1],num2)}")
                    # appends the answer to the answer list
                    answers.append(calculation(answers[len(answers)-1],num2))
                    # iterating condition
                    playon = input("Do you wish to perform more actions? (yes/no) ").lower()   
               else:
                    # break the for loop otherwiser
                    break
          elif continueplay == 'n':
               # asks the user for new input values
               num1, operationtype, num2 = user_input()
               if check_operationtype(operationtype):
                    print(f"{num1} {operationtype} {num2} = {calculation(num1,num2)}")
                    # appends the answer to the answer list 
                    answers.append(calculation(num1,num2))
                    # iterating condition
                    playon = input("Do you wish to perform more actions? (yes/no) ").lower()
               else:
                    # break the for loop otherwise
                    break

     print("Calulation terminated")

