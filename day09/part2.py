
disk_map = 0
fragmented = []
maxid = 0

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
        maxid = id
        for i in range(block):
            fragmented.append(int(id))

# print(fragmented)

def findNextFreeSpace(first, last):
    # select next free block
    if fragmented[first] == '.':
        while fragmented[first] == '.':
            first += 1

    while fragmented[first] != '.':
        first += 1
    last = first
    if last + 1 == len(fragmented):
        return first, last
    while fragmented[last + 1] == '.':
        last += 1

    return first, last


def findNextFileSpace(first, last, currentid):
    while fragmented[last] != int(currentid):
        last -= 1

    first = last

    if first-1 == 0:
        return first, last-1

    while fragmented[first - 1] == currentid:
        first -= 1

    return first, last





# defragmenteren
frontidfirst = 0
frontidlast = 0
backidlast = len(fragmented) - 1
backidfirst = len(fragmented) - 1
currentid = maxid


while currentid >= 0:
    # select file block
    # print(backidfirst, backidlast)
    backidfirst, backidlast = findNextFileSpace(backidfirst, backidlast, currentid)
    sizefile = backidlast+1 - backidfirst
    # print(f"check file block: {fragmented[backidfirst:backidlast+1]}, size: {sizefile}")

    # find free space
    fit = False
    frontidfirst = 0
    try:
        while not fit:
            frontidfirst, frontidlast = findNextFreeSpace(frontidfirst, frontidlast)
            # print(f"check free bloc: {len(fragmented[frontidfirst:frontidlast+1])}")
            sizefree = frontidlast+1 - frontidfirst
            # print(f"sizefree: {sizefree},  sizefile: {sizefile}")
            if sizefree >= sizefile:
                # print(fragmented)
                if frontidfirst < backidfirst:
                    for i in range(sizefile):
                        # print(f"{i}:{fragmented[backidlast+1]}")
                        # print(i)
                        fragmented[frontidfirst+i] = fragmented[backidfirst+i]
                        fragmented[backidfirst+i] = '.'
                fit = True
    except IndexError:
        pass

    currentid -= 1

# print(fragmented)

# optellen
total = 0
for idx, item in enumerate(fragmented):
    if item != '.':
        total += int(item) * idx

print(f"part 2 = {total}")
