import sys
from collections import Counter

# read numbers
numbers = []

# group the numbers
counters = {}
# make the groups
for i in range(10):
    counters[i] = 0



with open('input.txt') as f:
    numbers = [int(x) for x in f.readline().split()]
print(numbers)

# apply the rules, always return list
def do_magic(number):
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        first = int(str(number)[:len(str(number))//2])
        second = int(str(number)[len(str(number))//2:])
        # print(f" full: {number}, first: {first}, second: {second}")
        return [first, second]
    else:
        return [number * 2024]

for i in range(75):
    print("Working on step ", i)
    new_numbers = []
    new_counters = {}
    # for i in range(10):
    #     new_counters[i] = 0
    for number in numbers:
        magic_numbers = do_magic(number)
        for magic_number in magic_numbers:
            if not magic_number in new_counters.keys():
                new_counters[magic_number] = 0
            new_counters[magic_number] += 1
            # if 0 <= magic_number < 10:
            #     new_counters[magic_number] += 1
            # else:
            #     new_numbers.append(magic_number)
    for number, amount in counters.items():
        if amount != 0:
            magic_numbers = do_magic(number)
        else:
            continue
        for magic_number in magic_numbers:
            if not magic_number in new_counters.keys():
                new_counters[magic_number] = 0
            new_counters[magic_number] += amount
            # if 0 <= magic_number < 10:
            #     new_counters[magic_number] += amount
            # else:
            #     for i in range(amount):
            #         new_numbers.append(magic_number)

    # add up the new values to the totals
    numbers = new_numbers
    counters = new_counters

    # print(f"Step {i} : {len(numbers)} numbers")
    # print("------")
    # print(numbers)



print("Part 2 = " ,sum(counters.values()))




