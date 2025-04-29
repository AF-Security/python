# random


import random

number = random.randint(1, 10)

print(number)


# random.shuffle(x), will shuffle the list x, the argument, in place
# random.choice(x), will randomly select an element from the list x
# random.sample(x, k), will randomly select k elements from the list x
# random.randint(a, b), will randomly select an integer between a and b, inclusive

cards = ["jack", "queen", "king"]
# this is defining a list in order
random.shuffle(cards)
# this will shuffle the list in place
for card in cards:
    # the for loop iterates through the list, printing cards one at a time
    # one line at a time, since we are using print
    print(card)







# average

import statistics

print(statistics.mean([100,90]))

