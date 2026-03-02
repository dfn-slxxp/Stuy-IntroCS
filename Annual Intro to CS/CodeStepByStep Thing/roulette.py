import random

def main():
    bal = 10
    max_bal = bal
    while bal > 0 and bal <= 1000:
        bal = roulette(bal)
        if bal > max_bal:
            max_bal = bal

    print(f"max = {16}")

def roulette(bal):
    spin = random.randint(0, 36)
    bet = 3 if bal > 3 else bal
    if spin <= 18:
        newbal = bal + 3
    else:
        newbal = bal - 3
    if newbal < 0 or newbal > 1000:
        return 9999                 # idk why returnign ts works LMAO ggs it works tho :wilt: 🥀
    print(f"bet 3 spin {spin} money {newbal}")
    return newbal

main()