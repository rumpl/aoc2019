

def from_place(graph, start):
    v = start
    seen = []
    while True:
        parent = graph[v]
        v = parent
        if parent == "COM":
            break
        seen.append(parent)
    return seen


def count_path(f, t):
    total = 0
    for n in f:
        if n in t:
            break
        total += 1
    return total


graph = dict()

with open('input.txt') as f:
    for line in f.readlines():
        [a, b] = line.split(')')
        graph[b.strip()] = a.strip()

you = from_place(graph, 'YOU')
san = from_place(graph, 'SAN')

print(count_path(you, san) + count_path(san, you))
