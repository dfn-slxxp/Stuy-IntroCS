def print_pay(salary, hours):
    if hours <= 8:
        print(f"Hours worked: {hours}")
        print(f"Pay earned: $ {salary * hours}")
    else:
        print(f"Hours worked: {hours}")
        print(f"Pay earned: $ {salary * 8 + (1.5 * salary * (hours-8))}")