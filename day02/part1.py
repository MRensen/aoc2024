import re


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def is_sorted2(lst):
    try:
        for i in range(len(lst) - 1):
            if not (lst[i] < lst[i + 1]):
                if not (lst[i] < lst[i + 2]):
                    return False
        return True
    except IndexError:
        return is_sorted2(lst[::-1])

    # errors = sum(
    #     lst[i] > lst[i + 1]
    #     for i in range(len(lst) - 1)
    # )
    # return errors


input = []
with open("input.txt") as f:
    input = [[int(word) for word in re.split(r'\s+', line) if word.strip()] for line in f]


# def part1(input):
#     result = {}
#     for index, report in enumerate(input):
#         if (is_sorted(report) or is_sorted(report[::-1])):
#             if (all(report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] >= 1 for i in range(len(report) - 1))
#                     or all(report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] >= 1 for i in
#                            range(len(report) - 1))):
#                 result[index] = True
#             else:
#                 result[index] = False
#         else:
#             result[index] = False
#     # print(result)
#     return result

def part1(input):
    result = {}
    for index, report in enumerate(input):

            violations = 0
            for i in range(len(report) - 1):
                if not (1 <= report[i] - report[i + 1] <= 3 or 1 <= report[i + 1] - report[i] <= 3):
                    violations += 1
            check3 = is_sorted(report)
            check4 = is_sorted(report[::-1])
            if not(check3 or check4):
                violations += 1

        # if (is_sorted(report) or is_sorted(report[::-1])):
        #     if (all(report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] >= 1 for i in range(len(report) - 1))
        #             or all(report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] >= 1 for i in
        #                    range(len(report) - 1))):
            if (violations <= 0):
                result[index] = True
            else:
                result[index] = False
        # else:
        #     result[index] = False
    print(result)
    return result


def part2(input):
    result = {}

    for index, report in enumerate(input):
        counter = 0
        # if is_sorted2(report, counter) or is_sorted2(report[::-1], counter):

        violations = 0
        violations = check_range(report, violations)
        check3 = is_sorted2(report)
        check4 = is_sorted2(report[::-1])
        if not (check3 or check4):
            violations += 1
        # violations += min(check3, check4)

        if violations <= 0:
            result[index] = True
        else:
            result[index] = False
        # else:
        #     result[index] = False
        # print("iter")
    print(result)
    return result


def check_range(report, violations):
    for i in range(len(report) - 1):
        if not (1 <= report[i] - report[i + 1] <= 3 or 1 <= report[i + 1] - report[i] <= 3):
            try:
                if not (1 <= report[i] - report[i + 2] <= 3 or 1 <= report[i + 2] - report[i] <= 3):
                    violations += 1
            except IndexError:
                return check_range(report[:-1:], violations)
    return violations


print(len([x for x, y in part1(input).items() if y]))
print(len([x for x, y in part2(input).items() if y]))

# print(result)
