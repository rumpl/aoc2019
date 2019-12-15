from itertools import permutations
from os import system

class Alarm:
    def __init__(self, input):
        self.input = []
        for i in input:
            self.input.append(i)
        for i in range(0, 10000):
            self.input.append(0)
        self.pc = 0
        self.base = 0

    def get_param(self, pos):
        m = self.modes.pop(0)
        if m == 0:
            return self.input[pos]

        if m == 1:
            return pos

        return self.input[pos] + self.base

    def get(self, pos):
        return self.input[self.get_param(pos)]

    def add(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        c = self.get_param(self.pc + 3)
        self.input[c] = a + b
        self.pc += 4

    def mul(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        c = self.get_param(self.pc + 3)#
        self.input[c] = a * b
        self.pc += 4

    def read(self):
        val = input("value:")
        a = self.get_param(self.pc + 1)
        self.input[a] = int(val)
        self.pc += 2

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
        c = self.get_param(self.pc + 3)
        if a < b:
            self.input[c] = 1
        else:
            self.input[c] = 0

        self.pc += 4

    def eq(self):
        a = self.get(self.pc + 1)
        b = self.get(self.pc + 2)
        c = self.get_param(self.pc + 3)
        if a == b:
            self.input[c] = 1
        else:
            self.input[c] = 0

        self.pc += 4

    def rel(self):
        self.base += self.get(self.pc + 1)
        self.pc += 2

    def g(self, l, n):
        if n < 0:
            return 0
        try:
            return int(l[n])
        except IndexError:
            return 0

    def opcode(self):
        op = self.input[self.pc]
        o = str(op)
        l = len(o)
        return [op % 100, self.g(o, l - 3), self.g(o, l - 4), self.g(o, l - 5)]

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
                a = self.get_param(self.pc + 1)
                self.input[a] = int(val)
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
            elif opc == 9:
                self.rel()
            elif opc == 99:
                break
        yield None

class Robot:
    def __init__(self, p):
        self.panels = dict()
        for i in range(-100, 100):
            self.panels[i] = {}
            for j in range(-100, 100):
                self.panels[i][j] = -1
        self.p = p
        self.pos = [0, 0]
        self.direction = 0
        self.result = 0

    def get_panel_color(self):
        color = self.panels[self.pos[0]][self.pos[1]]
        if color == -1:
            return 0
        return color

    def set_panel_color(self, color):
        x = self.pos[0]
        y = self.pos[1]
        if self.panels[x][y] == -1:
            self.result += 1
        self.panels[x][y] = color

    def set_direction(self, d):
        if d == 0:
            self.direction = (self.direction - 1) % 4 
        if d == 1:
            self.direction = (self.direction + 1) % 4 

    def move(self, d):
        self.set_direction(d)
        if self.direction == 0:
            self.pos[1] -= 1
        if self.direction == 1:
            self.pos[0] += 1
        if self.direction == 2:
            self.pos[1] += 1
        if self.direction == 3:
            self.pos[0] -= 1

    def run(self):
        p = self.p.run()
        # c = 0
        while True:
            try:
                next(p)
                c = self.get_panel_color()
                color = p.send(c)
                d = next(p)
            except:
                break
            
            self.set_panel_color(color)
            self.move(d)
            c = self.get_panel_color()

inp = [3,8,1005,8,330,1106,0,11,0,0,0,104,1,104,0,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,28,1,1103,17,10,1006,0,99,1006,0,91,1,102,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,64,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,86,2,4,0,10,1006,0,62,2,1106,13,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,120,1,1109,1,10,1,105,5,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,1,8,10,4,10,1002,8,1,149,1,108,7,10,1006,0,40,1,6,0,10,2,8,9,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,187,1,1105,10,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,1002,8,1,213,1006,0,65,1006,0,89,1,1003,14,10,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,102,1,8,244,2,1106,14,10,1006,0,13,3,8,102,-1,8,10,1001,10,1,10,4,10,108,0,8,10,4,10,1001,8,0,273,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,1,8,10,4,10,1001,8,0,295,1,104,4,10,2,108,20,10,1006,0,94,1006,0,9,101,1,9,9,1007,9,998,10,1005,10,15,99,109,652,104,0,104,1,21102,937268450196,1,1,21102,1,347,0,1106,0,451,21101,387512636308,0,1,21102,358,1,0,1105,1,451,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21101,0,97751428099,1,21102,1,405,0,1105,1,451,21102,1,179355806811,1,21101,416,0,0,1106,0,451,3,10,104,0,104,0,3,10,104,0,104,0,21102,1,868389643008,1,21102,439,1,0,1105,1,451,21102,1,709475853160,1,21102,450,1,0,1105,1,451,99,109,2,22102,1,-1,1,21101,0,40,2,21101,482,0,3,21102,1,472,0,1105,1,515,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,477,478,493,4,0,1001,477,1,477,108,4,477,10,1006,10,509,1101,0,0,477,109,-2,2105,1,0,0,109,4,2101,0,-1,514,1207,-3,0,10,1006,10,532,21101,0,0,-3,21202,-3,1,1,22101,0,-2,2,21101,1,0,3,21101,0,551,0,1105,1,556,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,579,2207,-4,-2,10,1006,10,579,22102,1,-4,-4,1105,1,647,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,0,598,0,1106,0,556,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,617,21101,0,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,639,22102,1,-1,1,21102,1,639,0,105,1,514,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2105,1,0]
a = Alarm(inp)
r = Robot(a)
r.run()
print(r.result)
