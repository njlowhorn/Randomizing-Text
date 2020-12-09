import random

m = open("m.txt")
n = open("n.txt")

m1 = m.read(3)
n1 = n.read(3)

for a in m1:
    for b in n1:
        c = (a, b)
        d = random.choice(c)
        print(d)