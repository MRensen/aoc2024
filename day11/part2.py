
# group the numbers
counters = {}


# read numbers
with open('input.txt') as f:
    numbers = [int(x) for x in f.readline().split()]
    for num in numbers:
        # Put numbers in a map and count how often they would appear in the actual list of numbers
        # Assumption: there are no duplicate values in the input
        counters[num] = 1


# apply the rules, always return list
def do_magic(number):
    if number == 0:
        return [1]
    elif len(str(number)) % 2 == 0:
        num_len = len(str(number))//2
        first = int(str(number)[:num_len])
        second = int(str(number)[num_len:])
        return [first, second]
    else:
        return [number * 2024]

for i in range(75):
    print("Working on step ", i)
    new_counters = {} # temporary map, to not contaminate the loop
    # Go through all keys in the map and apply the magic.
    # Put the result of the magic as a new key and give it the value of the original key
    # or add it if it is already a key with a value.
    for number, amount in counters.items():
        if amount != 0:
            magic_numbers = do_magic(number)
        else:
            continue
        for magic_number in magic_numbers:
            if not magic_number in new_counters.keys():
                new_counters[magic_number] = 0
            new_counters[magic_number] += amount
    counters = new_counters




print("Part 2 = " ,sum(counters.values()))




