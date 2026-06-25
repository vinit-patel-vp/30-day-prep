#Day 1 - Python Basics Revision

#############################################################################
# Write a Python program that does all of this in one file:

# Create a variable for your name, age and city
# Print them using an f-string
# Create a list of 5 subjects you are studying
# Loop through the list and print each subject
# Write a function that takes two numbers and returns the larger one
# Write a conditional that checks if a number is even or odd
#############################################################################

name = "John Doe"
age = 27
city = "toronto"

print(f"Hello {name} your age is {age} years and you are from {city}")

subjects = ["calculus", "linear algebra", "statistics", "python", "web"]

for subject in subjects:
    print(subject)

num1 =5
num2 = 6  
def find_lrg_number (a,b):
   if a>b : return a   
   else : return b



largest_number = find_lrg_number(num1, num2)

print(f"{largest_number} is the largest number")

if largest_number%2 == 0: print ("Largest number is even")
else: print("largest number is odd")


