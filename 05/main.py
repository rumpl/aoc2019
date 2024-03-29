class Alarm:
    def __init__(self, input):
        self.input = input
        self.pc = 0

    def get(self, pos):
        m = self.modes.pop(0)
        if m == 0:
            return self.input[self.input[pos]]
        else:
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

    def read(self):
        val = input("value:")
        self.set(self.pc + 1, int(val))
        self.pc += 2

    def pp(self):
        print('pp:', self.get(self.pc + 1))
        self.pc += 2

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
                self.read()
            elif opc == 4:
                self.pp()
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

inp = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,72,20,224,1001,224,-1440,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1002,147,33,224,101,-3036,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,1102,32,90,225,101,65,87,224,101,-85,224,224,4,224,1002,223,8,223,101,4,224,224,1,223,224,223,1102,33,92,225,1102,20,52,225,1101,76,89,225,1,117,122,224,101,-78,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1102,54,22,225,1102,5,24,225,102,50,84,224,101,-4600,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1102,92,64,225,1101,42,83,224,101,-125,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,58,195,224,1001,224,-6840,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,1101,76,48,225,1001,92,65,224,1001,224,-154,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,226,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1107,226,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,8,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,389,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,404,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,419,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,434,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,449,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,7,677,677,224,102,2,223,223,1006,224,509,101,1,223,223,107,226,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,554,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,8,677,226,224,102,2,223,223,1006,224,584,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,1007,677,226,224,1002,223,2,223,1005,224,614,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,629,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,659,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]
a = Alarm(inp)
a.run()
