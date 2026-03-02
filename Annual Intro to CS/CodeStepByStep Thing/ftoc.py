# converts Fahrenheit temperatures to Celsius
def ftoc(tempf):
    tempc = (tempf - 32) * (5 / 9)
    return tempc

def main():
    tempf = 98.6
    tempc = ftoc(tempf)
    print("Body temp in C is:", tempc)

main()