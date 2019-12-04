start = 372037
end = 905157


def is_password(p):
    string = str(p)
    m = dict()
    f = string[0]
    m[int(f)] = 1
    string = string[1:]

    for s in string:
        if int(f) > int(s):
            return False
        m[int(s)] = m.get(int(s), 0) + 1
        f = s

    good = False
    for n in m.values():
        if n >= 2:
            good = True

    return good


total = 0
for i in range(start, end):
    if is_password(i):
        total += 1
print(total)
