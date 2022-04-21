#Please write a program which asks for the number of students on a course and the desired group size. The program will then print out the number of groups formed from the students on the course. If the division is not even, one of the groups may have fewer members than specified.

#If you can't get your code working as expected, it is absolutely okay to move on and come back to this exercise later. The topic of the next section is conditional statements. This exercise can also be solved using a conditional construction.

# Write your solution here
number_of_students= int(input("How many students on the course?"))
group_size=int(input("Desired group size?"))
number_groups= 1
if number_of_students%group_size ==0:
    number_groups= number_of_students//group_size
else:
    number_groups += (number_of_students//group_size)
print(f"Number of groups formed: {number_groups}")