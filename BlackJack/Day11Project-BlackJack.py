############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules (Casino) #####################

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)
# import modules
import itertools
import random

def pick_cards(numcards,userlist):
     '''
     Deal cards to players and remove them from the deck
     
     ----------
     parameters
     ----------
     
     numcards:     number of cards you want to pick from the deck
     userlist:     the player to give the cards to
     
     -------
     outputs
     -------
     
     stores the cards in the respective player's list    
     '''
     # using a for loop to deal the desired number of cards
     for i in range(1,numcards+1):
          # add the card to the player's list
          userlist.append(random.choice(deck))
          # removes the same card from the deck
          deck.remove(userlist[len(userlist)-1])

def find_total_score(userlist):              
     '''
     Finds the total score of a given player
     
     ----------
     parameters
     ----------
     
     userlist:     the player that you wish to inspect
     
     -------
     outputs
     -------
     
     calculates the total score 
     '''
     # initialise total to 0
     total = 0
     # use a for loop to loop through all the items in the list
     for item in userlist:
          if 'ace' in item:
               suit = item[1]
               # removes the item if it contains 'ace' and insert a 1 at the front of the list
               userlist.pop(int([userlist.index(item) for item in userlist if 'ace' in item][0]))
               userlist.insert(0,(1,suit))
     # use a for loop to loop through all the items in the list and calculate the total score
     for card in userlist:
          total += int(card[0])
     return total

def pick_right_total(num1,num2):
     '''
     Finds the total score of a given player
     
     ----------
     parameters
     ----------
     
     num1:     first number 
     num2:     second number
     
     -------
     outputs
     -------
     
     finds the most ideal score for victory conditions
     '''
     # use if statements to return the appropriate score based on given conditions if 2 score is acquired
     if num1 > 21:
          return num2
     elif num2 > 21:
          return num1 
     elif num1 == num2:
          return num1
     elif num2 < 21:
          return num2

#  creating all the unique values and suits
vals = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']
# creates a full deck of cards by multiplying all the values with all the suits and turns it into a list
deck = list(itertools.product(vals, suits))
# initialising an empty list for the player and the dealer
player = []
dealer =[]


# randomly chooses two cards for the player
pick_cards(numcards=2,userlist=player)
if player[0][0] == 'ace' or player[1][0] == 'ace':
     # prints the possible values if the player is dealt an 'ace'
     print(f"Your first card is {player[0]} and your second is {player[1]}\nYou have {find_total_score(player)} or {find_total_score(player) + 10}")
     playertotal1,playertotal = find_total_score(player),find_total_score(player)+10
else:
     # prints the values if not dealt an 'ace'
     print(f"Your first card is {player[0]} and your second is {player[1]}\nYou have {find_total_score(player)}")
     playertotal = find_total_score(player)


# randomly chooses one card for the dealer
pick_cards(numcards=1,userlist=dealer)
if dealer[0][0] == 'ace':
     # prints the possible values if the dealer is dealt an 'ace'
     print(f"Dealer's first card is {dealer[0]}. \nDealer has {find_total_score(dealer)} or {find_total_score(dealer) + 10}")
     dealertotal1,dealertotal2 = find_total_score(dealer),find_total_score(dealer)+10
else:
     # prints the values if not dealt an 'ace'
     print(f"Dealer's first card is {dealer[0]}. \nDealer have {find_total_score(dealer)}")
     dealertotal = find_total_score(dealer)

# check if the player has already been dealt a hand with blackjack
if playertotal == 21:
     print(f"Blackjack. Your total is {playertotal}.\nYou won")
else:
     keepplaying = input("Do you want to pick another card? (y/n): ").lower()
     if keepplaying =='n' and player[0][0] == 1:
          # store the more ideal value if the player is has an 'ace'
          finalplayertotal = pick_right_total(playertotal1,playertotal)
     else:
          # stores the current score as the final score
          finalplayertotal = playertotal
          
     while keepplaying == 'y':
          pick_cards(numcards=1,userlist=player)
          # if the picked card is an ace then print two possible values
          if player[len(player)-1][0] == 'ace':
               suit = player[len(player)-1][1]
               # remove the 'ace' 
               player.pop(int([player.index(item) for item in player if 'ace' in item][0]))
               # replaces the 'ace' with 1 at the beginning of the list
               player.insert(0,(1,suit))
               playertotal1,playertotal2 = find_total_score(player),find_total_score(player)+10
               # using if statements to check for all winning conditions and prints corresponding comments
               if playertotal1 == 21 or playertotal2 == 21:
                    print(f"Your card is {player[0]}.\nBlackjack. Your total is 21.\nYou won")
                    break
               elif len(player) == 5 and playertotal1 < 21 or len(player) == 5 and playertotal2 < 21:
                    print(f"Your card is {player[0]}.\nYour total is {playertotal1}, you did not exceeded 21 and you drew 5 cards. You won")
                    break
               elif playertotal1 > 21:
                    print(f"Your card is {player[0]}.\nYour total is {playertotal1}, you have exceeded 21. Game Over")
                    break
               else:
                    print(f"Your card is {player[0]}\nYour total is {playertotal1} or {playertotal2} ")
                    keepplaying = input("Do you want to pick another card? (y/n): ")
                    # if the player chooses to stop, then store the current value as the final total value
                    if keepplaying == 'n':
                         finalplayertotal = pick_right_total(playertotal1,playertotal2)
                         
          # if previous cards were 'ace' but this card is not then print the 2 possible total score             
          elif player[len(player)-1][0] != 'ace' and player[0][0] == 1:
               playertotal1,playertotal2 = find_total_score(player),find_total_score(player)+10
               # using if statements to check for all winning conditions and prints corresponding comments
               if playertotal1 == 21 or playertotal2 == 21:
                    print(f"Your card is {player[len(player)-1]}.\nBlackjack. Your total is {playertotal2}.\nYou won")
                    break
               elif len(player) == 5 and playertotal1 < 21 or len(player) == 5 and playertotal2 < 21:
                    print(f"Your card is {player[len(player)-1]}.\nYour total is {playertotal1}, you did not exceeded 21 and you drew 5 cards. You won")
                    break
               elif playertotal1 > 21:
                    print(f"Your card is {player[len(player)-1]}.\nYour total is {playertotal1}, you have exceeded 21. Game Over")
                    break
               else:
                    print(f"Your card is {player[len(player)-1]}\nYour total is {playertotal1} or {playertotal2} ")
                    keepplaying = input("Do you want to pick another card? (y/n): ")
                    # if the player chooses to stop, then store the current value as the final total value
                    if keepplaying == 'n':
                         finalplayertotal = pick_right_total(playertotal1,playertotal2)
                         
          # if no 'ace' were dealt then print the total score               
          elif player[len(player)-1][0] != 'ace' and player[0][0] != 1:
               playertotal = find_total_score(player)
               # using if statements to check for all winning conditions and prints corresponding comments
               if playertotal == 21:
                    print(f"Your card is {player[len(player)-1]}.\nBlackjack. Your total is {find_total_score(player)}.\nYou won")
                    break
               elif len(player) == 5 and playertotal < 21:
                    print(f"Your card is {player[len(player)-1]}.\nYour total is {find_total_score(player)}, you did not exceeded 21 and you drew 5 cards. You won")
                    break
               elif playertotal > 21:
                    print(f"Your card is {player[len(player)-1]}.\nYour total is {find_total_score(player)}, you have exceeded 21. Game Over")
                    break
               else:
                    print(f"Your card is {player[len(player)-1]}\nYou have {find_total_score(player)}")
                    keepplaying = input("Do you want to pick another card? (y/n): ")
                    # if the player chooses to stop, then store the current value as the final total value
                    finalplayertotal = playertotal
                    
     
     while keepplaying == 'n':
          
          pick_cards(numcards=1,userlist=dealer)
          # if the current card is 'ace'
          if dealer[len(dealer)-1][0] == 'ace':
               suit = dealer[len(dealer)-1][1]
               # removes the 'ace' from the list
               dealer.pop(int([dealer.index(item) for item in dealer if 'ace' in item][0]))
               # replaces the 'ace' with 1 at the beginning of the list
               dealer.insert(0,(1,suit))
               dealertotal1,dealertotal2 = find_total_score(dealer),find_total_score(dealer)+10
               # using if statements to check for all winning conditions and prints corresponding comments
               if dealertotal1 == 21 or dealertotal2 == 21:
                    print(f"Dealer's card is {dealer[0]}.\nBlackjack. Dealer's total is 21.\nDealer's won")
                    break
               elif dealertotal1 >= 17:
                    if dealertotal1 > finalplayertotal and dealertotal1 < 21:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal1} and your total is {finalplayertotal}.\nYou lost.")
                         break
                    elif dealertotal1 == finalplayertotal:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal1} and your total is {finalplayertotal}.\nIt's a tie.")
                         break
                    elif dealertotal1 < finalplayertotal:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal1} and your total is {finalplayertotal}.\nYou Won.")
                         break
               elif (len(dealer) == 5 and dealertotal1 < 21) or (len(dealer) == 5 and finalplayertotal < 21):
                    print(f"Dealer's card is {dealer[0]}.\nDealer's total is {dealertotal1}, Dealer's did not exceeded 21 and you drew 5 cards. Dealer's won")
                    break
               elif dealertotal1 > 21:
                    print(f"Dealer's card is {dealer[0]}.\nDealer's total is {dealertotal1}, Dealer's have exceeded 21. Game Over")
                    break
               else:
                    print(f"Dealer's card is {dealer[0]}\nDealer's total is {dealertotal1} or {dealertotal2} ")

          # if any previous cards was an 'ace'
          elif dealer[len(dealer)-1][0] != 'ace' and dealer[0][0] == 1:
               dealertotal1,dealertotal2 = find_total_score(dealer),find_total_score(dealer)+10
               # using if statements to check for all winning conditions and prints corresponding comments
               if dealertotal1 == 21 or dealertotal2 == 21:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}.\nBlackjack. Dealer's total is {dealertotal2}.\nDealer's won")
                    break
               elif dealertotal1 >= 17:
                    if dealertotal1 > finalplayertotal and dealertotal1 < 21:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal1} and your total is {finalplayertotal}.\nYou lost.")
                         break
                    elif dealertotal1 == finalplayertotal:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal1} and your total is {finalplayertotal}.\nIt's a tie.")
                         break
                    elif dealertotal1 < finalplayertotal:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal1} and your total is {finalplayertotal}.\nYou Won.")
                         break
               elif len(dealer) == 5 and dealertotal1 < 21 or len(dealer) == 5 and dealertotal2 < 21:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer's total is {dealertotal1}, Dealer's did not exceeded 21 and you drew 5 cards. You won")
                    break
               elif dealertotal1 > 21:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer's total is {dealertotal1}, Dealer's have exceeded 21. Game Over")
                    break
               else:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}\nDealer's total is {dealertotal1} or {dealertotal2} ")

          # if there were no 'ace' dealt
          elif dealer[len(dealer)-1][0] != 'ace' and dealer[0][0] != 1:
               dealertotal = find_total_score(dealer)
               # using if statements to check for all winning conditions and prints corresponding comments
               if dealertotal == 21:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}.\nBlackjack. Dealer's total is {dealertotal}.\nDealer's won")
                    break
               elif dealertotal >= 17:
                    if dealertotal > finalplayertotal and dealertotal < 21:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal} and your total is {finalplayertotal}.\nYou lost.")
                         break
                    elif dealertotal == finalplayertotal:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal} and your total is {finalplayertotal}.\nIt's a tie.")
                         break
                    elif dealertotal < finalplayertotal:
                         print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer total is {dealertotal} and your total is {finalplayertotal}.\nYou Won.")
                         break
               elif len(dealer) == 5 and dealertotal < 21:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer's total is {dealertotal}, Dealer's did not exceeded 21 and you drew 5 cards. You lost")
                    break
               elif dealertotal > 21:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}.\nDealer's total is {dealertotal}, Dealer's have exceeded 21. Game Over")
                    break
               else:
                    print(f"Dealer's card is {dealer[len(dealer)-1]}\nDealer's have {dealertotal}")

