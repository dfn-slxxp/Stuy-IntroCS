from tkinter import Tk, simpledialog
from tkinter.messagebox import showinfo

root = Tk()
root.withdraw()

folks = {}

def read_ts():
    with open('capitals.txt') as son:
        for line in son:
            line = line.rstrip("\n")
            line1 = line.split()
            contry = line1[0]
            cit = line1[1]
            folks[contry] = cit

def write_ts(contry, cit):
    with open('capitals.txt', 'a') as son:
        son.write('\n' + contry + ' ' + cit)
    son.close()

read_ts()

while not False:
    con_try = simpledialog.askstring("Country", "Type name of a country:")

    if con_try in folks:
        res = folks[con_try]
        showinfo("Answer", f"The capital of {con_try} is {res}!")

    else:
        cit = simpledialog.askstring("Folk", f"son idk ts what is the capital of ts {con_try}")
        folks[con_try] = cit
        write_ts(con_try, cit)