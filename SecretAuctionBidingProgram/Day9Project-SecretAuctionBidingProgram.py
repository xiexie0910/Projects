# imports the modules for clearing the console
from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

# defined a function that asks the user for all the inputs
def user_input():
  name = input("What is your name? ")
  bidamount = int(input("What is your bid? $"))
  otherplayers = input("Are there more bidders? Type yes or no ").lower()
  return name, bidamount, otherplayers

# defines an empty list
auction = []
# calling user_input function for inputs
name, bidamount, otherplayers = user_input()
# appending the initial inputs to the auction list
auction.append({"name":name,"bidamount":bidamount})

while otherplayers == 'yes':
  # clears the console
  clear()
  # asks and stores the input of another user
  name, bidamount, otherplayers = user_input()
  auction.append({"name":name,"bidamount":bidamount})

# initializing the variable maxbid
maxbid = 0
# using for loop to loop through all the elements in the auction list
for i in range(0, len(auction)):
  # using if statement to find the maximum bid amount and the bidder
  if maxbid < auction[i]["bidamount"]:
    maxbid = auction[i]["bidamount"]
    maxbidder = auction[i]["name"]
# print the list and the result of the winner and their bid
print(auction)
print(f"The winner of the auction is {maxbidder} and he placed a bet of {maxbid}")

