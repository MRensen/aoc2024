
disk_map = 0
fragmented = []

with open("input.txt") as f:
    # print(len(f.readline()))
    disk_map = f.readline()

# translate to 00..11.. notation
for idx, str_block in enumerate(disk_map):
    block = int(str_block)
    if idx%2 !=0:
        for i in range(block):
            fragmented.append('.')
    else:
        id = idx/2
        for i in range(block):
            fragmented.append(int(id))

print(fragmented)

# defragmenteren
frontid = 0
backid = len(fragmented)-1
while True:
    if backid <= frontid:
        break
    while fragmented[frontid] != '.':
        frontid += 1

    if fragmented[backid] == '.':
        while fragmented[backid] == '.':
            backid -= 1

    if backid <= frontid:
        break

    fragmented[frontid] = fragmented[backid]
    fragmented[backid] = '.'
    backid -= 1

print(fragmented)

# optellen
total = 0
for idx, item in enumerate(fragmented):
    if item != '.':
        total += int(item) * idx

print(f"part 1 = {total}")


