import re

left = []
right = []
with open("input.txt") as f:
    for line in f:
        split = re.split(r'\s+', line)
        # split = line.split("\s+")
        left.append(int(split[0]))
        right.append(int(split[1]))

left = sorted(left)
right = sorted(right)

# PArt 1
total = 0
for i, l in enumerate(left):
    total += max(right[i], l) - min(right[i], l)

print(total)

# Part 2
remember = {}
counter = 0

for i in left:
    if i not in remember:
        remember[i] = right.count(i)*i
    counter += remember[i]
    print(f"{counter} - {remember[i]}")
print(counter)