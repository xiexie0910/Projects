from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()

runcoffeemachine = 'on'
while runcoffeemachine == 'on':
     drink = input(f"What can I get for you today? {menu.get_items()} ")

     if drink =='off':
          break
     elif drink == 'report':
          coffee.report()
          money.report()
     else:
          drink = menu.find_drink(drink)
          if coffee.is_resource_sufficient(drink):
               if money.make_payment(drink.cost):
                    coffee.make_coffee(drink)

