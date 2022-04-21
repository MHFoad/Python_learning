##Please write a program which asks for the hourly wage, hours worked, and the day of the week. The program should then print out the daily wages, which equal hourly wage multiplied by hours worked, except on Sundays when the hourly wage is doubled.
# Write your solution here
hourly_wages= float(input("Hourly wage:"))
working_hours=float(input("Hours worked:"))
day=input("Day of the week:")
if day!= "Sunday":
    wages = hourly_wages*working_hours
else:
    wages = hourly_wages*2*working_hours
print(f'Daily wages: {wages} euros')