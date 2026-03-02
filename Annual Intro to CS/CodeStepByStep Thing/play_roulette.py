import random

def play_roulette(bal, bet):
    max_bal = bal
    print(f"start with $ {bal} and bet up to $ {bet}")
    print("bet\t spin\t money")
    while bal > 0:
        bal = roulette(bal, bet)
        if bal > max_bal:
            max_bal = bal

    print(f"max money = $ {max_bal}")

def roulette(bal, max_bet):
    spin = random.randint(0, 36)
    bet = max_bet if bal >= max_bet else bal
    if spin % 2 == 0 and spin != 0:
        newbal = bal + bet
    else:
        newbal = bal - bet
    if newbal < 0 or newbal > 1000:
        return 9999                 # idk why returnign ts works LMAO ggs it works tho :wilt: 🥀
    print(f"{bet}\t{spin}\t{newbal}")
    return newbal

play_roulette(10, 3)