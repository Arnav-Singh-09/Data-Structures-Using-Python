from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, item):
        self.container.append(item)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


class Cube:
    def __init__(self, edge):
        self.edge = edge


class Game:
    def __init__(self, no_of_stack, cubes):
        self.count = 0
        self.no_of_stack = no_of_stack
        self.no_of_cube = len(cubes)
        if no_of_stack < 1:
            print("Invalid number of stacks!")
        else:
            self.stacks = []
            for i in range(0, no_of_stack):
                stack = Stack()
                self.stacks.append(stack)
            for cube in cubes:
                self.stacks[0].push(cube)

    def move(self, start, end, source, target, spare):
        if start == end:
            target.push(source.pop())
            self.count += 1
            print("Step No."+str(self.count))
            self.print_tower()
        else:
            self.move(start+1, end, source, spare, target)
            self.move(start, start, source, target, spare)
            self.move(start+1, end, spare, target, source)

    def print_tower(self):
        for i in range(0, len(self.stacks)):
            print("Stack", i + 1, ':', end=" ")
            for j in range(len(self.stacks[i].container) - 1, -1, -1):
                print(self.stacks[i].container[j].edge, end=' ')
            print()
        print()


cubes = []
for i in range(4,0,-1):
    cube = Cube(i)
    cubes.append(cube)
game = Game(3, cubes)
start = 0
end = game.stacks[0].size() - 1
source = game.stacks[0]
target = game.stacks[-1]
spare = game.stacks[1]
game.print_tower()
game.move(start, end, source, target, spare)