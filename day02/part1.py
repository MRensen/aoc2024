import re


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


input = []
with open("input.txt") as f:
    input = [[int(word) for word in re.split(r'\s+', line) if word.strip()] for line in f]


def part1(input):
    result = {}
    for index, report in enumerate(input):
        partpart1(index, report, result)
    # print(result)
    return result

def partpart1(index, report, result={}):
        if not index in result.keys():
            result[index] = 0
        violations = 0
        for i in range(len(report) - 1):
            if not (1 <= report[i] - report[i + 1] <= 3 or 1 <= report[i + 1] - report[i] <= 3):
                violations += 1
        check3 = is_sorted(report)
        check4 = is_sorted(report[::-1])
        if not(check3 or check4):
            violations += 1


        if (violations <= 0):
            result[index] = 0
        else:
            result[index] += 1

        return result


def addresult(result, out):
    for key in result.keys():
        if key in out:
            result[key] += out[key]

    return result

def part2(input):
    result = {}

    for index, report in enumerate(input):
        for n in range(len(report) - 1):
            result = addresult(partpart1(index, report[:n:]), result)
    # print(result)

    return result


print("Part1: ",len([x for x, y in part1(input).items() if y < 1]))
print("Part2: ", len([x for x, y in part2(input).items() if y < 1]))

