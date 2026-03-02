def birthday():
    print("""
This program tells you how many days
it will be until your next birthday.
""")
    
    td_month = input("What is the month (1-12)? ")
    td_day = input("What is the day   (1-31)? ")

    printInfo(td_month, td_day)

    print("Please enter your birthday:")
    bd_month = input("What is the month (1-12)? ")
    bd_day = input("What is the day   (1-30)? ")

    printInfo(bd_month, bd_day)

    print(f"Your next birthday is in {getAbsolute(bd_month, bd_day) - getAbsolute(td_month, td_day) if getAbsolute(bd_month, bd_day) - getAbsolute(td_month, td_day) > 0 else 365 - getAbsolute(td_month, td_day) + getAbsolute(bd_month, bd_day)} days.")

def get_prev_days(month):
    s = 0
    for i in range(month - 1):
        s += days_in_months[i]
    return s

days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getAbsolute(m, d):
    return get_prev_days(m) + d

def printInfo(m, d):
    print(f"{m}/{d} is day #{getAbsolute(m, d)} of 365. \n")

# class Day:
    
#     def __init__(self, month, d):
#         self.month = int(month)
#         self.d = int(d)

#     def getAbsolute(self):
#         return get_prev_days(self.month) + self.d
    
#     def printInfo(self):
#         print(f"{self.month}/{self.d} is day #{self.getAbsolute()} of 365. \n")

birthday()