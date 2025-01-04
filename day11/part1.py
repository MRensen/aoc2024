
# read numbers
numbers = []
with open('test.txt') as f:
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
    new_numbers = []
    for idx, number in enumerate(numbers):
        new_numbers.extend(do_magic(number))
    numbers = new_numbers
    print(f"Step {i} : {len(numbers)} numbers")
    print("------")

print("Part 1: ", len(numbers))

# test

from collections import Counter


# Count occurrences of each number
counter = Counter(numbers)

# Find numbers that appear only once
unique_numbers = [num for num, count in counter.items() if count == 1]

# Output the unique numbers
# print("Numbers that appear only once:", unique_numbers)
[print(item) for item in sorted(counter.items())]