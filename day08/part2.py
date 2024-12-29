
posmap = {}
antinodescheat = [] #for testing purposes
antinodes = set()
mapsize = 0

with open("input.txt") as f:
    for x, line in enumerate(f):
        mapsize = len(line)-1
        for y, char in enumerate(line.strip()):
            if char == '#':
                antinodescheat.append((x, y)) # for testing
                continue
            if char != '.':
                if char not in posmap:
                    posmap[char] = []
                posmap[char].append((x,y))
                antinodescheat.append((x,y)) # for testing

print(mapsize)
print(len(posmap))
print(antinodescheat)
print(f"len {len(antinodescheat)}")


def inmap(inmapnode):
    x,y = inmapnode[0], inmapnode[1]
    return x >= 0 and y >= 0 and x <= mapsize and y <= mapsize


def calculateanti(node, othernode):
    antilist = []
    # De nodes zijn zelf ook antinodes in part2 (mits er minimaal 2 van die soort zijn, wat zo is als je al in deze functie terecht komt)
    antilist.append(node)
    antilist.append(othernode)
    x1, y1 = node
    x2, y2 = othernode

    # difference
    dx = x2 - x1
    dy = y2 - y1

    anti_x = x2
    anti_y = y2

    while True:
    # Calculate the anti node position
        anti_x = anti_x + dx  # Opposite direction along `dx`
        anti_y = anti_y + dy  # Opposite direction along `dy`
        anti = (anti_x, anti_y)
        if inmap(anti):
            antilist.append(anti)
        else:
            break
    return antilist


for char in posmap.keys():
    nodes = posmap[char]
    for node in nodes:
        for othernode in nodes:
            if othernode != node:
                #anti1 en anti2 zijn lists
                anti1: list = calculateanti(node, othernode)
                anti2: list = calculateanti(othernode, node)
                anti1.extend(anti2)
                for anti in anti1:
                    if anti is not None:
                        antinodes.add(anti)
                # print(f"{char} - {anti1}, {anti2}")
print(antinodes)
print(f"Part 2 : {len(antinodes)}")