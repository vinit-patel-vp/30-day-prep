# Create a dictionary with 3 key-value pairs (name, age, city) and print each value using a loop
# Write a function that takes a list of numbers and returns the sum without using sum()
# Write a function that checks if a string is a palindrome (same forwards and backwards)

#############################################################################

student = {"name" : "vinit",
           "age" : "23",
           "city" : "navsari"}

for key,values in student.items():
    print(key, values)

list_of_numbers = [1,2,3,4,5,6,7,8,9]

def add_list (numbers):
    total = 0 
    for number in numbers:
        total = number + total
    
    return total

list_total = add_list(list_of_numbers)
print(list_total)

def palindrome_check(word):
    rev_word = word[::-1]
    if rev_word == word:
        print("the given word is a palindrome")
    else:
        print("The given word is not a palindrome")

palindrome_check("yay")
palindrome_check("racer")