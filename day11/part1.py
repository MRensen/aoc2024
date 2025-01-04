
# read numbers
numbers = []
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
        return [first, second]
    else:
        return [number * 2024]

for i in range(25):
    new_numbers = []
    for idx, number in enumerate(numbers):
        new_numbers.extend(do_magic(number))
    numbers = new_numbers
    print(f"Step {i} : {len(numbers)} numbers")
    print("------")

print("Part 1: ", len(numbers))
