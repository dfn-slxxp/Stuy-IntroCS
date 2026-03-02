def show_two(n):
    if n % 2 != 0:
        print(n)
    else:
        print("2 * ", end="")
        show_two(n // 2)

def show_twos(n):
    print(f"{n} = ", end="")
    show_two(n)