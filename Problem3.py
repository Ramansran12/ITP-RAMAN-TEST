#ramandeep singh
#id 22076254
num_pennies = int(input("Enter the number of pennies: "))
num_nickels = int(input("Enter the number of nickels: "))
num_dimes = int(input("Enter the number of dimes: "))
num_quarters = int(input("Enter the number of quarters: "))

PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

num_pennies= (num_pennies * PENNY_VALUE)
num_nickels= (num_nickels * NICKEL_VALUE) 
num_dimes= (num_dimes * DIME_VALUE)
num_quarters= (num_quarters * QUARTER_VALUE)
total_cent= (num_pennies + num_nickels + num_dimes + num_quarters)
total_dollars = total_cent/PENNIES_IN_DOLLAR

if total_dollars > 100:
    print("Sorry, the amount you entered was more than one dollar.")
elif total_dollars < 100:
    print("Sorry, the amount you entered was less than one dollar.")
else:
    print("The amount you entered was exactly one dollar! You win the          game!!")
