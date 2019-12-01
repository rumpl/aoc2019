import math
import fileinput


def fuel(mass):
    if mass <= 0:
        return 0
    f = int(math.floor(int(mass) / 3) - 2)
    if f < 0:
        f = 0
    return f + fuel(f)


total = 0
for mass in fileinput.input():
    total += fuel(mass)

print(total)
