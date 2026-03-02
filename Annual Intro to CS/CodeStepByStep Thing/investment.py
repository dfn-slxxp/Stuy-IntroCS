def investor(i):
    print(f"Investor {i}")
    initial = float(input("Initial amount? "))
    rate = float(input("Interest rate%? "))
    months = int(input("Num. of months? "))

    f = round(initial * ((1 + rate) ** months), 2)

    print(f"Amount: $ {f}")

    profit = round(f - initial, 2)
    prof_percent = int(round(100 * profit / initial, 0))

    print(f"Profit: $ {profit} = {prof_percent} %")

    if (prof_percent < 10):
        pr("Weak")
    elif (prof_percent < 50):
        pr("Medium")
    else:
        pr("Strong")

    pr("")

def pr(str): # must define 3 functions my ass
    print(str)

def investment():
    investor(1)
    investor(2)

    print("Have a nice day!")

investment()