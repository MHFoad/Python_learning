##Please write a program which asks for the user's name. If the name is anything but "Jerry", the program then asks for the number of portions and prints out the total cost. The price of a single portion is 5.90.

# Write your solution here
name= input("Please tell me your name:")
if name == "Jerry":
    print("Next please!")
else:
    soup_portions= int(input("How many portions of soup?"))
    cost_per_portion= 5.90
    total_cost= soup_portions*cost_per_portion
    print(f"The total cost is {total_cost}\nNext please!")