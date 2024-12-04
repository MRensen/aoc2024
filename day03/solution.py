import re

puzzle = []
with open("input.txt") as f:
    puzzle = f.read()

def filterpuzzle(line):
    x = re.findall(r"mul\(\d+,\d+\)", line)
    y = [(line.find(j),j) for j in x]
    do = []
    flag = True
    for i in range(len(line)-1):
        if line[i: i+len("do()")] == "do()":
            flag = True
        if line[i: i+len("don't()")] == "don't()":
            flag = False
        if flag:
            do.append(i)



    return x, [mul for pos, mul in y if pos in do]

def parseresult(result):
    count = 0
    for i, res in enumerate(result):
        try:
            count += int(res[4:str(res).index(","):]) * int(res[res.index(",")+1:res.index(")"):])
        except Exception:
            pass
    return count


def parse(puzzle):
    result = filterpuzzle(puzzle)
    print(result[0])
    print("Part1: ", parseresult(result[0]))
    print("Part2: ", parseresult(result[1]))

parse(puzzle)