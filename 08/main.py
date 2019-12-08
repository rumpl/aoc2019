import sys

width = 25
height = 6


def layer(str):
    return str[0:width*height]


def get_pixel(layerss, x, y):
    for layer in layers:
        p = int(layer[x + y * width])
        if p != 2:
            return p

    return None


layers = []
with open('img.sif') as file:
    line = file.read().strip()
    while True:
        layers.append(layer(line))
        line = line[width*height:]
        if len(line) == 0:
            break

ps = {
    0: '⚫️',
    1: '⚪️'
}

for y in range(0, height):
    for x in range(0, width):
        pixel = get_pixel(layers, x, y)
        print(ps[pixel], end=" ")
    print()
