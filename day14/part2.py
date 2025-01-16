
# test grid is 11x7
# actual grid is 101x103

grid_width = 0
grid_height = 0
grid = []
filename = "input.txt"
with open(filename) as f:
    # set length and width
    if filename == "test.txt":
        grid_width ,grid_height = 11, 7
    else:
        grid_width ,grid_height = 101, 103

    robots = []

    # read robots from input
    for line in f:
        p,v = line.split(' ')
        p = [int(x) for x in p[2::].strip().split(',')]
        v = [int(x) for x in v[2::].strip().split(',')]
        robots.append([p,v])
        # print(f"{p=}, {v=}")

def printgrid(step=None):
    grid = [[' '] * grid_width for _ in range(grid_height)]
    string_map = []
    found_pattern  = False
    for robot in robots:
        grid[robot[0][1]][robot[0][0]] = '*'
    for row in grid:
        string_line = "".join(map(str, row))
        string_map.append(string_line)
        if "***************" in string_line:
            print("found: step ",step)
            found_pattern = True
    if found_pattern:
        for row_line in string_map:
            print(row_line)
        print(f"*************************************** step{step} ***********************************************")
        print('\n')
        return step
    else:
        return None


# move the robots
step = 0
result = False
while not result:
    step += 1
    for robot in robots:
        x,y = robot[0]
        i,j = robot[1]
        new_x = (x+i) % grid_width
        new_y = (y+j) % grid_height
        robot[0] = [new_x,new_y]
    result = printgrid(step)

print("The result for part 2 = ", result)











