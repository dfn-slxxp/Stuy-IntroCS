def pay(salary, hours):
    if hours <= 8:
        return salary * hours
    else:
        return salary * 8 + (1.5 * salary * (hours-8))