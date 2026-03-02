def bmi_person(i):
    print(f"Person {i} information:")

    height = float(input("height (in inches)? "))
    weight = float(input("weight (in pounds)? "))

    bmi = round(703 * (weight / (height ** 2)), 1)

    print(f"BMI = {bmi}")

    if bmi < 18.5:
        bmi_class = 1
    elif bmi < 25:
        bmi_class = 2
    elif bmi < 30:
        bmi_class = 3
    else:
        bmi_class = 4

    print(f"class {bmi_class}")

    print("")

def say_nice_day(): # screw 3 functyiona lmasodaoj
    print("Have a nice day!")

def bmi():
    print("This program reads data for two people")
    print("and computes their body mass index (BMI).")
    print("")
    
    bmi_person(1)
    bmi_person(2)

    say_nice_day()

bmi()