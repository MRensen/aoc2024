
# test grid is 11x7
# actual grid is 101x103
SEC = 100 # constant (robots take 100 steps)

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

    # Make grid todo: maybe unnecessary
    # grid = [[0] * grid_width for _ in range(grid_height)]
    robots = []

    # read robots from input
    for line in f:
        p,v = line.split(' ')
        p = [int(x) for x in p[2::].strip().split(',')]
        v = [int(x) for x in v[2::].strip().split(',')]
        robots.append([p,v])
        # print(f"{p=}, {v=}")

# move the robots
for robot in robots:
    for _ in range(0,SEC):
        x,y = robot[0]
        i,j = robot[1]
        new_x = (x+i) % grid_width
        new_y = (y+j) % grid_height
        robot[0] = [new_x,new_y]
        # print(new_x, new_y)


# count them up
count = [0,0,0,0]
for robot in robots:
    x,y = robot[0]
    A = count[0]
    B = count[1]
    C = count[2]
    D = count[3]
    halfx = int(grid_width/2)
    halfy = int(grid_height/2)
    if x < halfx and y < halfy:
        count[0] += 1
    elif x > halfx and y > halfy:
        count[3] += 1
    elif x < halfx and y > halfy:
        count[2] += 1
    elif x > halfx and y < halfy:
        count[1] += 1

def printgrid():
    grid = [[0] * grid_width for _ in range(grid_height)]
    for robot in robots:
        grid[robot[0][1]][robot[0][0]] += 1
    for row in grid:
        print(" ".join(map(str, row)))



def mult(lis):
    cum = 1
    for l in lis:
        cum *= l
    return cum

total_count = mult(count)
print(count, "xhalf= " , int(grid_width/2), " yhalf= " , int(grid_height/2))
# printgrid()
[print(robot[0]) for robot in robots]
print("answer to part 1 is: ", total_count)





