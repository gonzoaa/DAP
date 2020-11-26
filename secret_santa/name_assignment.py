import numpy as np 


import random

l = ["Marky", "Diego", "Ronni", "Jake", "Luna", "Isa" , "Nava" ]

pairs = {}

while len(l) > 1:

    #Using the randomly created indices, respective elements are popped out
    r1 = random.randrange(0, len(l))
    elem1 = l.pop(r1)

    r2 = random.randrange(0, len(l))
    elem2 = l.pop(r2)

    # now the selecetd elements are paired in a dictionary 
    pairs[elem1] = elem2

#The variable 'pairs' is now a dictionary of this form:
#{'Sister': 'Aunt', 'Uncle': 'Father', 'Mother': 'Brother'}

##We can now print the elements of the dictionary in your desired format:
i = 1

for key, value in pairs.items():
    print("Pair {}: {} and {}".format(i, key, value))
    i += 1
