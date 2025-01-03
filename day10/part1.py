#find the path
# as long as possible
# even, gradual, uphill slope
# starts at 0 ends at 9, increase of 1 each step
# no diagonals

guide = []
starters = {}


# read map
with open("input.txt") as f:
    for line in f:
        guide.append(list(line.strip()))

# find starters
for i, line in enumerate(guide):
    for j, val in enumerate(line):
        if guide[i][j] == "0":
            starters[i,j] = []


# calculate path
def find_next(i, j):
    current = int(guide[i][j])
    result = []
    dirs = [(0,1), (1,0), (-1,0), (0,-1)]
    for i_plus, j_plus in dirs:
        if i + i_plus < 0 or j + j_plus < 0 or i + i_plus >= len(guide) or j + j_plus >= len(guide[0]):
            continue
        else:
            next = int(guide[i + i_plus][j + j_plus])
            if (next - current) == 1:
                result.append((i+i_plus, j+j_plus))
    return result


def calc_path(path, i, j):
    if path is None or len(path) == 0:
        return path
    last = path[-1]
    last_val = guide[last[0]][last[1]]
    if last_val == "9":
        return path
    nextnext = find_next(path[-1][0], path[-1][1])
    print(f"{nextnext=}")
    for next in nextnext:
        arg = path.copy()
        arg.append(next)
        new_path = calc_path(arg, i, j)
        print(f"{new_path=}")
        if new_path != None:
            starters[(i, j)].append(new_path)

    print("\n")





for x,y in starters.keys():

    next:list = find_next(x, y)
    print(f"next={next}")

    for n in next:
        print(f"{n=}")
        new_path = calc_path([n], x, y)
        print(f"new_path={new_path}")
        if new_path != None:
            starters[(x, y)].append(new_path)


# count score
def count_score(trail_heads):
    counter = set([trail[-1] for trail in trail_heads])
    return len(counter)


print(f"{starters=}")
counter = 0
counter2 = 0
for starter in starters.keys():
    # print([guide[i][j] for i, j in set([trail[-1] for trail in starters[starter]])])
    # print([x for x in set([trail[-1] for trail in starters[starter]])])
    counter += count_score(starters[starter])
    counter2 += len(starters[starter])

print(f"part 1 = {counter}")
print(f"part 2 = {counter2}")




