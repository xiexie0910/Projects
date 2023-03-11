#If the bill was $150.00, split between 5 people, with 12% tip. 
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
numpeople = int(input("How many people to split the bill? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
payperperson = (bill / numpeople) * (1+tip/100)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# the following line is to ensure that the number is also rounded to 2dp
finalcost = "{:.2f}".format(round(payperperson,2))
print("Each person should pay: $",finalcost)
#Write your code below this line 👇


