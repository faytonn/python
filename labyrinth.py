import sys


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.dx, self.y + other.dy)


class Direction:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def turnRight(self):
        return Direction(-self.dy, self.dx)

    def turnLeft(self):
        return Direction(self.dy, -self.dx)

    def goForward(self, position):
        return Position(position.x + self.dx, position.y + self.dy)


def directionFromSymbol(symbol):
    if symbol == "^":
        return Direction(0, -1)
    elif symbol == "v":
        return Direction(0, 1)
    elif symbol == "<":
        return Direction(-1, 0)
    elif symbol == ">":
        return Direction(1, 0)


def symbolFromDirection(d):
    if d.dx == 0 and d.dy == -1:
        return "^"
    elif d.dx == 0 and d.dy == 1:
        return "v"
    elif d.dx == -1 and d.dy == 0:
        return "<"
    elif d.dx == 1 and d.dy == 0:
        return ">"


def isOpenCell(maze, position):
    return maze[position.y][position.x] != "X"


def printMaze(maze):
    for row in maze:
        print("".join(row))
    print()


def main():
    n = int(sys.stdin.readline().strip())
    mazeLines = sys.stdin.read().split("\n")
    mazeLines = [line for line in mazeLines if line]

    maze = [list(row) for row in mazeLines]

    beastPosition = None
    beastDirection = None
    foundBeast = False

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] in "^>v<":
                beastPosition = Position(x, y)
                beastDirection = directionFromSymbol(maze[y][x])
                maze[y][x] = "."
                foundBeast = True
                break
        if foundBeast:
            break

        justTurnedRight = False
    for _ in range(n):
        rightDirection = beastDirection.turnRight()
        forwardPosition = beastDirection.goForward(beastPosition)
        rightPosition = beastPosition + rightDirection
        
        if justTurnedRight == True:
            if isOpenCell(maze, forwardPosition):
                beastPosition = forwardPosition
            else:
                beastDirection = beastDirection.turnLeft()
                
            justTurnedRight = False
                
        else:
            if isOpenCell(maze, rightPosition):
               beastDirection = beastDirection.turnRight()
               justTurnedRight = True
            elif isOpenCell(maze, forwardPosition):
                beastPosition = forwardPosition
            else:
               beastDirection = beastDirection.turnLeft()

        maze[beastPosition.y][beastPosition.x] = symbolFromDirection(beastDirection)
        printMaze(maze)
        maze[beastPosition.y][beastPosition.x] = "."


if __name__ == "__main__":
    main()
