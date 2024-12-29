
posmap = {}
antinodescheat = [] # for testing purposes
antinodes = set()
mapsize = 0

with open("input.txt") as f:
    for x, line in enumerate(f):
        mapsize = len(line)-1
        for y, char in enumerate(line.strip()):
            if char == '#':
                antinodescheat.append((x, y))
                continue
            if char != '.':
                if char not in posmap:
                    posmap[char] = []
                posmap[char].append((x,y))

print(antinodescheat)
print(mapsize)
print(len(posmap))


def inmap(inmapnode):
    x,y = inmapnode[0], inmapnode[1]
    return x >= 0 and y >= 0 and x < mapsize and y < mapsize


def calculateanti(node, othernode):
    x1, y1 = node
    x2, y2 = othernode

    # difference
    dx = x2 - x1
    dy = y2 - y1

    # Calculate the anti node position
    anti_x = x2 + dx  # Opposite direction along `dx`
    anti_y = y2 + dy  # Opposite direction along `dy`

    anti = (anti_x, anti_y)
    return anti if inmap(anti) else None


for char in posmap.keys():
    nodes = posmap[char]
    for node in nodes:
        for othernode in nodes:
            if othernode != node:
                anti1 = calculateanti(node, othernode)
                anti2 = calculateanti(othernode, node)
                for anti in (anti1, anti2):
                    if anti is not None:
                        antinodes.add(anti)
                # print(f"{char} - {anti1}, {anti2}")
print(antinodes)
print(f"Part 1 : {len(antinodes)}")