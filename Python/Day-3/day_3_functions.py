###############################################################################
# Build a program that is a simple BMI Calculator that:

# Has a function that takes weight and height and returns BMI
# Has a function that takes BMI and returns the category:
# weight(kg) / height(m)²
# Below 18.5 → Underweight
# 18.5 to 24.9 → Normal
# 25 to 29.9 → Overweight
# 30 and above → Obese


# Has a function that prints a full report:

# Name
# Weight
# Height
# BMI (rounded to 2 decimal places)
# Category
###############################################################################

def calculate_bmi(height, weight):
    
    bmi = weight/(height*height)
    return bmi

def bmi_category_display(bmi):
            if 0<= bmi < 18.5:
                return "UnderWeight"
            elif 18.5<= bmi <25:
                return "Normal"
            elif 25<= bmi <30:
                return "Overweight"
            elif bmi >= 30 :
                return "Obese"
            else: print("enter a valid value")


def bmi_input(name, height, weight):

    bmi = calculate_bmi(height, weight)
    category = bmi_category_display(bmi)

    print("Name : ", name)
    
    print(f"Bmi : {bmi:.2f}")

    print("Category: ", category)


name = input("\nEnter your Name")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi_input(name, height, weight)


name = input("\nEnter your Name")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi_input(name, height, weight)


name = input("\nEnter your Name")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi_input(name, height, weight)

    
    
        



    





