##Please write a program which estimates a user's typical food expenditure.

#The program asks the user how many times a week they eat at the student cafeteria. Then it asks for the price of a typical student lunch, and for money spent on groceries during the week.

#Based on this information the program calculates the user's typical food expenditure both weekly and daily.
# Write your solution here
number_meals_per_week= int (input("How many times a week do you eat at the student cafeteria?"))
price= float(input("The price of a typical student lunch?"))
groceries_spend_per_week= float(input("How much money do you spend on groceries in a week?"))
Food_cost_weekly= (number_meals_per_week*price)+groceries_spend_per_week
print(f"Average food expenditure:\nDaily: {Food_cost_weekly/7} euros\nWeekly: {Food_cost_weekly} euros")