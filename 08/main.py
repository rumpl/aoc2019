import sys

width = 25
height = 6

digits = {
    0: 0,
    1: 0,
    2: 0
}

layer_digits = []


def layer(str):
    return str[0:width*height]


def group_sum(line):
    digits = {
        0: 0,
        1: 0,
        2: 0
    }

    for l in line:
        digits[int(l)] += 1

    return digits


with open('img.sif') as file:
    line = file.read().strip()
    while True:
        l = layer(line)
        layer_digits.append(group_sum(l))
        line = line[width*height:]
        if len(line) == 0:
            break

m = sys.maxsize
imin = -1
for i in range(0, len(layer_digits)):
    l = layer_digits[i]
    if l[0] < m:
        m = l[0]
        imin = i

print(layer_digits[imin][1] * layer_digits[imin][2])
