import random

def random_walk(threshold):
    pos = 0
    max_pos = pos
    steps = 0
    while pos > -threshold and pos < threshold:
        pos = roulette(pos)
        if pos > max_pos:
            max_pos = pos
        steps += 1    
        
    print(f"Finished after {steps-1} step(s)")
    print(f"Max position = {max_pos}")

def roulette(bal):
    spin = random.randint(0,1)
    spin = -1 if spin == 0 else 1
    newbal = bal + spin
    if newbal < 0 or newbal > 1000:
        return bal                 # idk why returnign ts works LMAO ggs it works tho :wilt: 🥀
    print(f"Position = {newbal}")
    return newbal

random_walk(3)