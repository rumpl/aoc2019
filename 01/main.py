import math
import fileinput


def fuel(mass):
    return int(math.floor(int(mass) / 3) - 2)


total = 0
for mass in fileinput.input():
    total += fuel(mass)

print(total)
