print("What is the weather forecast for tomorrow?")
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
print("Wear jeans and a T-shirt")
if temperature < 21:
    print("I recommend a jumper as well")
if temperature < 11:
    print("Take a jacket with you")
if temperature < 6:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")
if rain == "yes":
    print("Don't forget your umbrella!")
# Write your solution here
temp=int(input("What is the weather forecast for tomorrow?\nTemperature:"))
rain=input("Will it rain (yes/no):")
if temp>20:
    if rain=="no":
        print("Wear jeans and a T-shirt")
    else:
        print("Wear jeans and a T-shirt\nDon't forget your umbrella!")
if temp<=20 and temp>10:
    if rain=="no":
        print("Wear jeans and a T-shirt\nI recommend a jumper as well\n")
    else:
        print("Wear jeans and a T-shirt\nI recommend a jumper as well\nDon't forget your umbrella!")
if temp<=10 and temp>5:
    if rain=="no":
        print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you")
    else:
        print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nDon't forget your umbrella!")
if temp<=5:
    if rain=="no":
        print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order")
    else:
        print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order\nDon't forget your umbrella!")

