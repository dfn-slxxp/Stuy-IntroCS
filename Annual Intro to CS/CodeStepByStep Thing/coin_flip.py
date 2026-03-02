import random

def coin_flip(x, f):
    if f not in ["H", "T"] or x < 0:
        print("ERROR!")
        return
    
    target = 0 if f == "H" else 1
    
    count = 0
    while count < x:
        flip = random.randint(0, 1)
        print("H" if flip == 0 else "T",end = " ")
        if flip == target:
            count += 1
        else:
            count == 0
    print("")
    print(f"You got {f} {x} times in a row!")