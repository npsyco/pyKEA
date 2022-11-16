import os
class Bird:
    def __init__(self, start, dir):
        self.pos = start
        # left: 3; right: 1; up: 4; down: 2
        self.dir = dir

        # methods
        self.methods = {"f":self.fwd, "l":self.left, "r":self.right}



    def fwd(self):
        if self.dir == 1:
            # [2,2] -> [2,3]
            self.pos[1] = self.pos[1] + 1
        elif self.dir == 2:
            self.pos[0] = self.pos[0] + 1
        elif self.dir == 3:
            self.pos[1] = self.pos[0] - 1
        else:
            self.pos[0] = self.pos[0] - 1

    def left(self):
        if self.dir == 1:
            self.dir = 4
        else:
            self.dir -= 1

    def right(self):
        if self.dir == 4:
            self.dir = 1
        else:
            self.dir += 1

    def loose(self):
        return "Bird loses!"

    def __repr__(self):
        return f"{self.__dict__}"

class Pig:
    def __init__(self, pos):
        self.pos = pos
        self.is_alive = True

    def death(self):
        return "Pig's Dead!"

class Board:
    def __init__(self):
        self.bird = Bird([2, 2], 1)
        self.c = Bird.__dict__
        self.pig = Pig([2, 5])

    def run(self, cmd):
        for i in cmd:
            self.bird.methods[i]()

    def display(self, ):
        os.system('cls')
        for i in range(1, 11):
            for j in range(1, 11):
                if (i, j) == tuple(self.bird.pos):
                    print("B", end=" ")
                elif (i, j) == tuple(self.pig.pos):
                    print("P", end=" ")
                else:
                    print("*", end= " ")
            print()

class Workspace:
    def __init__(self):
        self.moves = None

    def display(self):
        print("\nEnter Move")
        print("Options: Forward(f), Turn Left (l), Turn Right (r)")
        print("Type 'q' to quit")

    def commands(self):
        self.display()
        l = []
        q = True
        b = Board()
        # while q:
        x = input("Move: ")
        if x == "q":
            q = False
        else:
            l.append(x)

        print(len(l))



        return l

class Game:
    
    def main(self):
        b = Board()
        b.display()

        w = Workspace()
        # w.display()

        l = w.commands()
        while len(l) != 0:
            b.run(l)
            b.display()

            if b.bird.pos == b.pig.pos:
                b.pig.death()
                print(f"Birds position: {b.bird.pos}")
                print(f"Pigs position: {b.pig.pos}")
                break
            l = w.commands()
        print(self.win(b))


    def win(self, b):
        if b.bird.pos == b.pig.pos:
            return b.pig.death()
        else:
            return b.bird.loose()


if __name__ == '__main__':
    g = Game()
    g.main()
