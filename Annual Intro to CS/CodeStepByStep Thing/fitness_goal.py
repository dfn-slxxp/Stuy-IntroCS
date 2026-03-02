def fitness_goal(days):
    print(f"Train until you increase for {days} days.")
    days_increased = 1
    total_days = 0
    prev_day = 9999
    while days_increased < days:
        mins = int(input("Minutes? "))
        print("Great job!" if mins > prev_day or total_days == 0 else "Start over.")
        days_increased += 1 if mins > prev_day else 0
        if mins < prev_day and total_days != 0:
            days_increased = 0
        prev_day = mins
        total_days += 1
    print(f"Reached your goal in {total_days} total days!")