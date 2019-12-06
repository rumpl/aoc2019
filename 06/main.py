
graph = dict()

with open('input.txt') as f:
    for line in f.readlines():
        [a, b] = line.split(')')
        graph[b.strip()] = a.strip()

total = 0
for v in graph:
    if v == "COM":
        continue
    while True:
        parent = graph[v]
        v = parent
        total += 1
        if parent == "COM":
            break

print(total)
