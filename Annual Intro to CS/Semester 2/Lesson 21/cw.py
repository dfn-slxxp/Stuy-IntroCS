def read_file():
    file = open('something.txt')
    text = file.read()
    print(text)

def read_first_n():
    n = int(input("How many lines?\n"))
    text = open('something.txt').read().split('\n')[:n]
    print(text)

def read_last_n():
    n = int(input("How many lines?\n"))
    l = open('something.txt').read().split('\n')
    text = l[len(l) - n:]
    print(text)

def read_to_list():
    return open('something.txt').read().split('\n')

def count_lines_from_file():
    return len(open('something.txt').read().split('\n'))