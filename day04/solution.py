import re

puzzle = []
with open("input.txt") as f:
    puzzle = [list(x) for x in list(f.read().split("\n"))]

def part1():
    found = 0
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            temp=found
            if puzzle[row][col] == "X":
                found += checkForXMAS(row, col, puzzle, False)
                found += checkForXMAS(row, col, puzzle, True)
            # if not found == temp:
            #     print(f"({row}, {col}, {found})")
    return found

def checkForXMAS(row, col, puzzle, reversed):
    found = 0
    a = puzzle[row][col]
    vert = [a]
    horz = [a]
    diagu = [a]
    diagd = [a]
    for x in range(1,4):
        if not reversed:
            expected = 'XMAS'
            dirs = [x if x >= 0 else None for x in [row-x, col-x, col+x]]
        else:
            expected = 'XMAS'
            dirs = [x if x >= 0 else None for x in[row+x, col+x, col-x]]
        try:
            vert.append(puzzle[row][dirs[1]])
        except (IndexError, TypeError):
            # print("indexerror")
            pass
        try:
            horz.append(puzzle[dirs[0]][col])
        except (IndexError, TypeError):
            # print("indexerror")
            pass
        try:
            diagu.append(puzzle[dirs[0]][dirs[1]])
        except (IndexError, TypeError):
            # print("indexerror")
            pass
        try:
            diagd.append(puzzle[dirs[0]][dirs[2]])
        except (IndexError, TypeError):
            # print("indexerror")
            pass
        if col == 5 and row == 0:
            print(diagu, diagd, vert, horz)
    for direction in [vert, horz, diagu, diagd]:
        if ''.join(direction) == expected:
            found += 1
    # if col==1 and row==9:
    # print(vert, horz, diagu, diagd)
    return found

def part2():
    found = 0
    for row in range(len(puzzle)):
        for col in range(len(puzzle[row])):
            # temp=found
            if puzzle[row][col] == "A":
                found += checkForX_MAS(row, col, puzzle)
            # if not found == temp:
            #     print(f"({row}, {col}, {found})")
    return found


def getLetter(puzzle, row, col):
    if col<0 or row<0:
        return None
    try:
        x = puzzle[row][col]
        if x == "M" or x == "S":
            return x
        return None
    except IndexError:
        return None


def checkForX_MAS(row, col, puzzle):

    a = puzzle[row][col]
    lu = getLetter(puzzle, row-1, col-1)
    ld = getLetter(puzzle, row-1, col+1)
    ru = getLetter(puzzle, row+1, col-1)
    rd = getLetter(puzzle, row+1, col+1)
    # if(row == 4 and col == 4):
    #     print(lu, ld, ru, rd)

    if ((lu == 'M' and rd == 'S') or (lu == 'S' and rd == 'M')) and ((ld == 'M' and ru == 'S') or (ld == 'S' and ru == 'M')):
        return 1
    else:
        return 0

print(part1())
print(part2())