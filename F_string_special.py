def personal_details(name,age,email,phone_number):
    print(f"{name}\n{age}\n{email}\n{phone_number}")
name= input("Please enter your Name:")
age= input("Enter the age:")
email= input("What is your email address:")
phone_number=input("May I know your contact number?:")
myinfo= personal_details(name,age,email,phone_number)
print(f"My name is {name}, I am {age} years old.")
print(f"Please give me your contact info.\nHere it is \nemail:{email} \nand \nphone number: {phone_number}")


