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






print(f"Part 1: {total_price}")