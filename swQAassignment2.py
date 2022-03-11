
def bmicalc():
    height = float(input("input height in inches: "))

    weight = float(input("input weight in pounds: "))

    weight = weight * 0.45

    height = height * 0.025

    height = height * height

    bmi = round((weight/height), 1)

    print("your BMI is: ")
    print(bmi)
    if bmi < 18.5:
        print("Category: Underweight")
    elif bmi >= 18.5 and bmi < 25: 
        print("Category: Normal Weight")
    elif bmi >= 25 and bmi < 30: 
        print("Category: Overweight")
    elif bmi >= 30: 
        print("Category: Obese")

    rs = input("Would you like to restart? (type y or n) ")
    if rs == 'y':
        bmicalc()
    else:
        exit()



bmicalc()