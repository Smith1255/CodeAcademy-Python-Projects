#adds up your food and drinks and gives a 20and 15% tip
 
#gets food price
food = float(input("How much did you spend on food?"))
 
#gets drink price
drink = float(input("How much did you spend on food"))
 
total = (food + drink)
 
print("\nyour total is:", total )
 
#asks the user if they want to tip 15% or 20%
print"""Would you like to be a nice person and tip 15%
           or be and awesome person and tip 20%
 

1.) 20%
 
2.) 15%
"""
 
#if the user picks 1 it will print toatl of 20% tip
#if the user picks two it will print total of 15% tip
choice = input("would you like choice 1 or 2?")
 
if choice == 2:
 print(.20 * total)
elif choice == 1:
 print(.15 *total)
else:
 print("\n I said 1 or 2")
