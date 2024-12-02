import re


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

input = []
with open("input.txt") as f:
    input = [[int(word) for word in re.split(r'\s+', line) if word.strip()] for line in f]

def part1(input):
    result = {}
    for index, report in enumerate(input):
        if(is_sorted(report) or is_sorted(report[::-1])):
            if(all(report[i] - report[i+1] <= 3 and report[i] - report[i+1] >= 1 for i in range(len(report)-1))
                    or all(report[i+1] - report[i] <= 3 and report[i+1] - report[i] >= 1 for i in range(len(report)-1))):
                result[index] = True
            else:
                result[index] = False
        else:
            result[index] = False
    # print(result)
    return result

def part2(input):
    # print(input)
    result = {}

    for index, report in enumerate(input):
        if(is_sorted(report) or is_sorted(report[::-1])):
            if(all(report[i] - report[i+1] <= 3 and report[i] - report[i+1] >= 1 for i in range(len(report)-1))
            or all(report[i+1] - report[i] <= 3 and report[i+1] - report[i] >= 1 for i in range(len(report)-1))):
                # result[index] = result.get(index, 1)
                # if result[index] > 1:
                #     result[index] = False
                # else:
                result[index] = result.get(index, 0) + 1
            else:
                result[index] = False
        else:
            result[index] = False

    return result


print(len([x for x, y in part1(input).items() if y]))
print(len([x for x,y in part2(input).items() if y]))

# print(result)

