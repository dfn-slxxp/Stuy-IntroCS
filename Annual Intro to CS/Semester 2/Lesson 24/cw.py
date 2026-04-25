import matplotlib.pyplot as son

fontdict = {"family" : "serif", "size" : 22, "weight" : "bold", "style" : "italic"}

bars = ["Grapes", "Blueberry", "Kiwifruit", "Banana", "Orange", "Apple"]
people = [5, 40, 25, 10, 30, 35]
colors = ["purple", "blue", "green", "yellow", "orange", "red"]

son.title("\"Nicest\" Fruit", fontdict=fontdict)

for i in range(6):
    son.barh(bars[i], people[i], color=colors[i])

son.xlabel("Number of People", fontdict=fontdict)
son.xticks(family='cursive')
son.yticks(family='cursive')

son.show()