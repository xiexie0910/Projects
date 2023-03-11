logo = '''_________         _____  _____                  _____                .__    .__               
\_   ___ \  _____/ ____\/ ____\____   ____     /     \ _____    ____ |  |__ |__| ____   ____  
/    \  \/ /  _ \   __\\   __\/ __ \_/ __ \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\     \___(  <_> )  |   |  | \  ___/\  ___/  /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \______  /\____/|__|   |__|  \___  >\___  > \____|__  (____  /\___  >___|  /__|___|  /\___  >
        \/                        \/     \/          \/     \/     \/     \/        \/     \/ 
        
          '''
print(logo)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coffeemachine(drinkstring):
     '''
     this function executes all the functions in the coffeemachine such as calculating the cost and subtracting the ingredients
     
     ----------
     Parameters
     ----------
     
     drinkstring:   string that contains the drink the user wants to drink
     
     -------
     Outputs
     -------
     
     executes all the commands in the coffeemachine
     '''
     # using if statements to check if there is enoguh water, coffee or milk
     if resources['water'] < MENU[drinkstring]['ingredients']['water']:
          print("Sorry, there is not enough water")
     elif resources['coffee'] < MENU[drinkstring]['ingredients']['coffee']:
          print("Sorry, there is not enough coffee")
     elif resources['milk'] < MENU[drinkstring]['ingredients']['milk']:
          print("Sorry, there is not enough milk")
     else:
          # subtracting the resources and asks for coin inputs
          resources['water'] -= MENU[drinkstring]['ingredients']['water']
          resources['coffee'] -= MENU[drinkstring]['ingredients']['coffee']
          resources['milk'] -= MENU[drinkstring]['ingredients']['milk']
          quarters = float(input("Please insert coins\nQuarters: ")) * 0.25
          dimes = float(input("Please insert coins\nDimes: ")) * 0.1
          nickles = float(input("Please insert coins\nNickles: ")) * 0.05
          pennies = float(input("Please insert coins\nPennies: ")) * 0.01
          money = quarters + dimes + nickles + pennies
          # checking if the user has inputted enough coins
          if money < MENU[drinkstring]['cost']: 
               print("Sorry that's not enough money. Money refunded.")
          else:
               # subtracting the cost and returning the change 
               money -= MENU[drinkstring]['cost']
               global machinemoney
               machinemoney += MENU[drinkstring]['cost']
               print(f"Here is ${round(money,2)} dollars in change.\nHere is your {drinkstring}. Enjoy!")
               
# initialize the while loop variable and money in the machine
runcoffeemachine = 'on'
machinemoney =0

while runcoffeemachine == 'on':
     
     drink = input("What drink can I get for you today? (expresso (e)/latte (l)/cappuccino (c)): ")
     if drink =='off':
          runcoffeemachine =='off'
     elif drink == 'report':
          print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${round(machinemoney,2)}")
     elif drink == 'e':
          # using if statements to check if there is enoguh water or coffee
          if resources['water'] < MENU["espresso"]['ingredients']['water']:
               print("Sorry, there is not enough water")
          elif resources['coffee'] < MENU["espresso"]['ingredients']['coffee']:
               print("Sorry, there is not enough coffee")
          else:
               # subtracting the resources and asks for coin inputs
               resources['water'] -= MENU["espresso"]['ingredients']['water']
               resources['coffee'] -= MENU["espresso"]['ingredients']['coffee']
               quarters = float(input("Please insert coins\nQuarters: ")) * 0.25
               dimes = float(input("Please insert coins\nDimes: ")) * 0.1
               nickles = float(input("Please insert coins\nNickles: ")) * 0.05
               pennies = float(input("Please insert coins\nPennies: ")) * 0.01
               money = quarters + dimes + nickles + pennies
               # checking if the user has inputted enough coins
               if money < MENU['espresso']['cost']: 
                    print("Sorry that's not enough money. Money refunded.")
               else:
                    # subtracting the cost and returning the change 
                    money -= MENU['espresso']['cost']
                    machinemoney += MENU['espresso']['cost']
                    print(f"Here is ${round(money,2)} dollars in change.\nHere is your espresso. Enjoy!")

     elif drink == 'c':
          # call the coffeemachine function
          coffeemachine('cappuccino')
               
     elif drink == 'l':
          # call the coffeemachine function
          coffeemachine('latte')