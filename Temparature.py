##Please write a program which asks the user for a temperature in degrees Fahrenheit, and then prints out the same in degrees Celsius. If the converted temperature falls below zero degrees Celsius, the program should also print out "Brr! It's cold in here!".

# Write your solution here
Temp_in_Fahrenheit= int (input("Please type in a temperature (F):"))
Temp_in_celsius= (Temp_in_Fahrenheit-32)*5/9
print(f'{Temp_in_Fahrenheit} degrees Fahrenheit equals {Temp_in_celsius} degrees Celsius')
if Temp_in_celsius<0:
    print("Brr! It's cold in here!")