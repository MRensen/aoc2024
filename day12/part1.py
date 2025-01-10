# Price = area * perimeter
# Total price of test.txt = 140
# Total price of test2.txt = 772
# Total price of test3.txt = 1930

grid = []
chars = set()
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
total_price = 0


with open('input.txt') as f:
    for line in f:
        # make (value, visited) pairs
        temp = []
        for char in line.strip():
            chars.add(char)
            temp.append((char, False))
        grid.append(temp)

print(grid)
print(chars)


def out_of_bounds(i,j):
    return i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0
def calc(i, j):
    total_area = 1 #start with 1 because i,j isn't counted otherwise
    total_perimeter = 0
    value = grid[i][j][0]
    grid[i][j] = (value, True)
    for dir in dirs:
        new_i = i + dir[0]
        new_j = j + dir[1]
        if out_of_bounds(new_i,new_j):
            total_perimeter += 1
            continue
        next_value = grid[new_i][new_j]
        if next_value[0] != value[0]:
            total_perimeter += 1
            continue
        if next_value[1]: # already visited
            continue
        else:
            next_next_value = calc(new_i, new_j)
            total_area += next_next_value[0]
            total_perimeter += next_next_value[1]

    return total_area, total_perimeter



for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j][1]:
            continue
        else:
            area, perimeter = calc(i,j)
            total_price += area * perimeter
            print(f" ({i},{j}): {grid[i][j]}, area: {area}, perim: {perimeter}")


 # (0,0): ('A', True), area: 28, perim-len: 14, perim: [[(1, 5, 's')], [(3, 0, 's'), (4, 0, 's')], [(3, 4, 'w'), (3, 3, 'w')], [(3, 3, 'n'), (4, 3, 'n')], [(3, 5, 's'), (4, 5, 's'), (5, 5, 's'), (0, 5, 's'), (2, 5, 's')], [(2, 2, 'e'), (2, 1, 'e')], [(4, 0, 'n')], [(0, 4, 'e'), (0, 3, 'e')], [(0, 3, 'w'), (0, 1, 'w'), (0, 5, 'w'), (0, 0, 'w'), (0, 4, 'w'), (0, 2, 'w')], [(0, 0, 'n'), (1, 0, 'n'), (2, 0, 'n'), (5, 0, 'n'), (3, 0, 'n')], [(2, 2, 's'), (1, 2, 's')], [(5, 2, 'e'), (5, 4, 'e'), (5, 1, 'e'), (5, 3, 'e'), (5, 5, 'e'), (5, 0, 'e')], [(5, 1, 'w'), (5, 2, 'w')], [(2, 5, 'n'), (1, 5, 'n')]]
 #
 # (0,0): ('A', True), area: 28, perim-len: 15, perim: [[(5, 0, 'n')], [(1, 5, 'n'), (2, 5, 'n')], [(0, 3, 'w')], [(2, 2, 's'), (1, 2, 's')], [(5, 3, 'e'), (5, 2, 'e')], [(3, 3, 'n'), (4, 3, 'n')], [(2, 2, 'e'), (2, 1, 'e')], [(0, 0, 'w'), (0, 2, 'w'), (0, 4, 'w'), (0, 1, 'w'), (0, 5, 'w')], [(5, 4, 'e'), (5, 1, 'e'), (5, 5, 'e'), (5, 0, 'e')], [(3, 4, 'w'), (3, 3, 'w')], [(0, 4, 'e'), (0, 3, 'e')], [(5, 2, 'w'), (5, 1, 'w')], [(3, 0, 's'), (4, 0, 's')], [(0, 5, 's'), (1, 5, 's'), (2, 5, 's'), (3, 5, 's'), (4, 5, 's'), (5, 5, 's')], [(0, 0, 'n'), (1, 0, 'n'), (2, 0, 'n'), (3, 0, 'n'), (4, 0, 'n')]]



print(f"Part 1: {total_price}")