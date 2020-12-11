import random

'''Opens the texts'''
m = open("m.txt")
n = open("n.txt")

'''Gets the first three characters of each text'''
m1 = m.read(3)
n1 = n.read(3)

'''Randomizes the characters'''
for a in m1:
    for b in n1:
        c = (a, b)
        d = random.choice(c)
        print(d)