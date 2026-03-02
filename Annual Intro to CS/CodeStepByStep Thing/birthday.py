def birthday():
    print("This program tells you how many days")
    print("it will be until your next birthday.")
    print("")
    
    print("Please enter today's date:")
    td_month = int(input("What is the month (1-12)? "))
    if (td_month in [1,3,5,7,8,10,12]):
        m = 31
    elif (td_month in [4,6,9,11]):
        m = 30
    else:
        m = 28
    td_day = (input(f"What is the day   (1-{m})? "))

    printInfo(td_month, td_day)

    print("Please enter your birthday:")
    bd_month = int(input("What is the month (1-12)? "))
    if (bd_month in [1,3,5,7,8,10,12]):
        m = 31
    elif (bd_month in [4,6,9,11]):
        m = 30
    else:
        m = 28
    bd_day = int(input(f"What is the day   (1-{m})? "))

    printInfo(bd_month, bd_day)

    days_left = getAbsolute(bd_month, bd_day) - getAbsolute(td_month, td_day) if getAbsolute(bd_month, bd_day) - getAbsolute(td_month, td_day) > 0 else 365 - getAbsolute(td_month, td_day) + getAbsolute(bd_month, bd_day)
    if (days_left == 1):
        print("Wow, your birthday is tomorrow!")
        return
    elif(days_left in [0, 365]):
        print("Happy birthday!")
        return
    print(f"Your next birthday is in {getAbsolute(bd_month, bd_day) - getAbsolute(td_month, td_day) if getAbsolute(bd_month, bd_day) - getAbsolute(td_month, td_day) > 0 else 365 - getAbsolute(td_month, td_day) + getAbsolute(bd_month, bd_day)} days.")

def get_prev_days(month):
    s = 0
    for i in range(month - 1):
        s += days_in_months[i]
    return s

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getAbsolute(m, d):
    return get_prev_days(m) + int(d)

def printInfo(m, d):
    print(f"{m}/{d} is day #{getAbsolute(m, d)} of 365. \n")

birthday()