from itertools import permutations 

class Alarm:
    def __init__(self, input):
        self.input = input
        self.pc = 0

    def get(self, pos):
        m = self.modes.pop(0)
        if m == 0:
            return self.input[self.input[pos]]
        return self.input[pos]

    def set(self, pos, val):
        self.input[self.input[pos]] = val

    def add(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        self.set(self.pc + 3, a + b)
        self.pc += 4

    def mul(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        self.set(self.pc + 3, a * b)
        self.pc += 4

    def pp(self):
        val = self.get(self.pc + 1)
        self.pc += 2
        return val

    def jit(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        if a != 0:
            self.pc = b
        else:
            self.pc += 3

    def jif(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        if a == 0:
            self.pc = b
        else:
            self.pc += 3

    def lt(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        c = self.input[self.pc + 3]
        if a < b:
            self.input[c] = 1
        else:
            self.input[c] = 0

        self.pc += 4

    def eq(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        c = self.input[self.pc + 3]
        if a == b:
            self.input[c] = 1
        else:
            self.input[c] = 0

        self.pc += 4

    def g(self, l, n):
        if n < 0:
            return 0
        try:
            return int(l[n])
        except IndexError:
            return 0

    def opcode(self):
        op = self.input[self.pc]
        ops = [
            [0],
            [1, 0, 0, 0],
            [2, 0, 0, 0],
            [3, 0],
            [4, 0],
            [5, 0, 0, 0],
            [6, 0, 0, 0],
            [7, 0, 0, 0],
            [8, 0, 0, 0]
        ]
        if op == 99:
            return [99]
        if op <= 8:
            return ops[op]

        o = str(op)
        return [op % 10, self.g(o, len(o) - 3), self.g(o, len(o) - 4), self.g(o, len(o) - 4)]

    def run(self):
        while True:
            op = self.opcode()
            opc = op[0]
            self.modes = op[1:]
            if opc == 1:
                self.add()
            elif opc == 2:
                self.mul()
            elif opc == 3:
                val = yield
                self.set(self.pc + 1, int(val))
                self.pc += 2
            elif opc == 4:
                out = self.pp()
                yield out
            elif opc == 5:
                self.jit()
            elif opc == 6:
                self.jif()
            elif opc == 7:
                self.lt()
            elif opc == 8:
                self.eq()
            elif opc == 99:
                break

        yield None

def feedback(inp, phases):
    # setup with initial values
    programs = [a.run() for a in [
            Alarm(inp.copy()),
            Alarm(inp.copy()),
            Alarm(inp.copy()),
            Alarm(inp.copy()),
            Alarm(inp.copy())
        ]
    ]

    for i in range(0, len(programs)):
        next(programs[i])
        programs[i].send(phases[i])

    phase = 0
    while True:
        for i in range(0, len(programs)):
            last = phase
            try:
                phase = programs[i].send(phase)
                next(programs[i])
            except StopIteration:
                return last


# Don't judge me...
inputs = permutations([5,6,7,8,9])
inp = [3,8,1001,8,10,8,105,1,0,0,21,38,55,68,93,118,199,280,361,442,99999,3,9,1002,9,2,9,101,5,9,9,102,4,9,9,4,9,99,3,9,101,3,9,9,1002,9,3,9,1001,9,4,9,4,9,99,3,9,101,4,9,9,102,3,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,102,2,9,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

max_out = 0
# phase = 0
for i in inputs:
    out = feedback(inp, i)
    if max_out < out:
        max_out = out

print(max_out)
