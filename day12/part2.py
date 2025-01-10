# Price = area * perimeter
# Total price of test.txt = 140
# Total price of test2.txt = 772
# Total price of test3.txt = 1930

grid = []
chars = set()
dirs = [(0, 1, 's'), (1, 0, 'e'), (0, -1, 'n'), (-1, 0, 'w')]
total_price = 0


with open('test4.txt') as f:
    for line in f:
        # make (value, visited) pairs
        temp = []
        for char in line.strip():
            chars.add(char)
            temp.append((char, False)) # add dict to keep track check if directions have been calculated for perimeter of a letter
        grid.append(temp)

# print(grid)
# print(chars)


def out_of_bounds(i,j):
    return i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0

def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


def calc(i, j):
    perimeter_list = []
    # perimeter_list.append((i,j))
    total_area = 1 #start with 1 because i,j isn't counted otherwise
    total_perimeter = 0
    value = grid[i][j][0]
    # grid_dict = grid[i][j][2]
    grid[i][j] = (value, True)
    for dir in dirs:
        new_i = i + dir[0]
        new_j = j + dir[1]
        if out_of_bounds(new_i,new_j):
            # add_perim(i,j,1)
            perimeter_list.append((i,j,dir[2]))
            continue
        next_value = grid[new_i][new_j]
        if next_value[0] != value[0]:
            # add_perim(i,j,1)
            perimeter_list.append((i,j, dir[2]))
            continue
        if next_value[1]: # already visited
            continue
        else:
            next_next_value = calc(new_i, new_j)
            total_area += next_next_value[0]
            perimeter_list.append(next_next_value[1])
            # add_perim(i,j,next_next_value[1])

    return total_area, perimeter_list




def calculate_sides(perimeter_coords: list):
    # dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    chains = []
    start = perimeter_coords.pop(0)
    next = start
    chain = [start]
    while len(perimeter_coords) > 0:
        found = None
        for dir in dirs:
            to_check = (next[0]+dir[0], next[1]+dir[1])
            if to_check in perimeter_coords and next[2]==to_check[2]:
                found = perimeter_coords.pop(perimeter_coords.index(to_check))
                chain.append(found)
                next = found

        if not found:
            chains.append(chain)
            next = perimeter_coords.pop(0)
            chain = [next]
        # print("chain:",chain)
    chains.append(chain)
    # print("chains:",chains)
    return chains



def calculate_connections(perimeter):
    '''
    Deze functie checkt voor elk coord in de perim welke coords daar bij aansluiten.
    Daarbij houd ie rekening met richting.
    :param perimeter: een lijst met alle coordinaten in de perimeter
    :return: De coordinaten van de zijdes van de areas, gesorteerd in lijsten. (len() == hoeveelheid zijden)
    '''
    chain = []
    chains = []
    to_check = perimeter.pop(0)
    chain.append(to_check)
    # print(to_check, ":", perimeter)
    for item in perimeter:
        if item[2] != to_check[2]: #check if same direction
            continue
        if to_check[2] == 'w' or to_check[2] == 'e': #if w/e check if same horizontal coordinate
            if to_check[0] == item[0]:
                chain.append(perimeter.pop(perimeter.index(item)))
        if to_check[2] == 's' or to_check[2] == 'n': # if n/s check if same vertical coordinate
            if to_check[1] == item[1]:
                chain.append(perimeter.pop(perimeter.index(item)))
    if len(perimeter) != 0:
        result = calculate_connections(perimeter)
        if isinstance(result, list):
            chains.extend(result)  # Add elements of the result to `chains` to avoid nesting
        else:
            chains.append(result)  # Append non-list results directly
    chains.append(chain)
    return chains

def fix_perimeter(perimeter):
    pass

def test(perim):
    for item in perim:
        print(f"len:{len(item)} :: {item}")

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j][1]:
            continue
        else:
            area, area_grid = calc(i,j)
            perimeter = calculate_sides(list(set(sorted(flatten_list(area_grid)))))
            perimeter_parts = calculate_connections([i[0] for i in perimeter])
            perimeter_fix = fix_perimeter(perimeter_parts)
            # total_price += area * perimeter
            print("sides section: ",len(perimeter_parts))
            print(perimeter_parts)
            # print(perimeter)
            # print(f" ({i},{j}): {grid[i][j]}, area: {area}, perim-len: {len(perimeter_parts)}, perim: {perimeter_parts}")
#





print(f"Part 2: {total_price}")
# print(grid)