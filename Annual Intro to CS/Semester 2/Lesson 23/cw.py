import matplotlib.pyplot as son

x = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

y1 = [1050, 1200, 800, 1350, 1400, 1510, 1050, 500, 1250]
y2 = [1550, 1650, 2300, 2010, 2300, 3010, 2250, 1490, 3000]

son.plot(x, y1, color="#5a9bd6", linewidth=3)
son.plot(x, y2, color="#ed7d30", linewidth=3)
son.title("Profit")
son.grid(axis='y')
son.show()