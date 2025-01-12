# Price = area * perimeter
# Total price of test.txt = 140
# Total price of test2.txt = 772
# Total price of test3.txt = 1930

grid = []
chars = set()
dirs = [(0, 1, 's'), (1, 0, 'e'), (0, -1, 'n'), (-1, 0, 'w')] #(x, y, richting)
total_price = 0


with open('input.txt') as f:
    for line in f:
        # make (value, visited) tuples
        temp = []
        for char in line.strip():
            chars.add(char)
            temp.append((char, False)) # add dict to keep track check if directions have been calculated for perimeter of a letter
        grid.append(temp)



# check if out of bounds
def out_of_bounds(i,j):
    return i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0

# Door de recursie krijg je lists in lists.
# Deze functie fixt dat. Misschien beter om de recursie er uit te halen.
def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list


# Deze functie berekend de Area en geeft de perimeter terug
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
        # If out of bounds, check volgende richting
        if out_of_bounds(new_i,new_j):
            perimeter_list.append((i,j,dir[2]))
            continue
        next_value = grid[new_i][new_j]
        # Als de naastgelegen coordinaat een andere letter (plant) is, dan is het een perimeter, maar geen area
        if next_value[0] != value[0]:
            perimeter_list.append((i,j, dir[2]))
            continue
        # Als het True is, dan is deze coord al eens eerder bekeken
        if next_value[1]:
            continue
        # Als het dat allemaal niet is, dan is het in de area.
        else:
            next_next_value = calc(new_i, new_j)
            total_area += next_next_value[0]
            perimeter_list.append(next_next_value[1])

    return total_area, perimeter_list

# De oude functie, die ik zelf had geschreven. Met recursie en een for-loop (en dubbele richting check)

# def calculate_connections(perimeter):
#     '''
#     Deze functie checkt voor elk coord in de perim welke coords daar bij aansluiten.
#     Daarbij houd ie rekening met richting.
#     :param perimeter: een lijst met alle coordinaten in de perimeter
#     :return: De coordinaten van de zijdes van de areas, gesorteerd in lijsten. (len() == hoeveelheid zijden)
#     '''
#     chain = []
#     chains = []
#     to_check = perimeter.pop(0)
#     chain.append(to_check)
#     # print(to_check, ":", perimeter)
#     for item in perimeter:
#         if item[2] != to_check[2]: #check if same direction
#             continue
#         if to_check[2] == 'w' or to_check[2] == 'e': #if w/e check if same horizontal coordinate
#             if to_check[0] == item[0]:
#                 chain.append(perimeter.pop(perimeter.index(item)))
#         if to_check[2] == 's' or to_check[2] == 'n': # if n/s check if same vertical coordinate
#             if to_check[1] == item[1]:
#                 chain.append(perimeter.pop(perimeter.index(item)))
#     if len(perimeter) != 0:
#         result = calculate_connections(perimeter)
#         if isinstance(result, list):
#             chains.extend(result)  # Add elements of the result to `chains` to avoid nesting
#         else:
#             chains.append(result)  # Append non-list results directly
#     chains.append(chain)
#     return chains

#Optimalisatie van chtgpt. Geen recursie en geen automatische iteratie met een for-loop.
# Nu een dubbele while loop.
# De binnenste while loop stapt handmatig (door middel van i++) door de perimeter en reset daarbij de loop-variabele na elke gevonden match.
# Een verdere (niet structureel belangrijke) optimalisatie is dat de richting check nu in 1 if-statement gebeurt.
def calculate_connections(perimeter):
    """
    Deze functie checkt voor elk coord in de perimeter welke coords daarbij aansluiten.
    Daarbij houdt hij rekening met richting.
    :param perimeter: een lijst met alle coordinaten in de perimeter
    :return: De coordinaten van de zijdes van de areas, gesorteerd in lijsten. (len() == hoeveelheid zijden)
    """
    chains = []

    while perimeter:
        # Start een nieuwe ketting met het eerste element
        chain = [perimeter.pop(0)]

        # Iteratief zoeken naar verbonden coördinaten
        to_check = chain[0]
        i = 0  # Index om te itereren door perimeter
        while i < len(perimeter):
            item = perimeter[i]

            if item[2] != to_check[2]:  # Controleer richting
                i += 1
                continue

            if (to_check[2] in ['w', 'e'] and to_check[0] == item[0]) or \
                    (to_check[2] in ['n', 's'] and to_check[1] == item[1]):
                # Voeg het item toe aan de huidige chain
                chain.append(perimeter.pop(i))
                # Start opnieuw met de controle vanaf het begin
                i = 0
            else:
                i += 1
        # print(sorted(chain))

        # Splits de keten op als coördinaten niet aaneengesloten zijn
        # (zorg dat je niet de 2 vlakken die toevallig boven elkaar liggen als 1 chain ziet, terwijl er eigenlijk afstand tussen zit.)
        corrected_chain = []
        idx = 0
        while idx < len(chain):
            current = sorted(chain)[idx]

            if corrected_chain and current[2] in ['w', 'e']:
                prev = corrected_chain[-1]
                if abs(current[1] - prev[1]) > 1:  # Breek keten
                    chains.append(corrected_chain)
                    corrected_chain = []
            elif corrected_chain and current[2] in ['n', 's']:
                prev = corrected_chain[-1]
                if abs(current[0] - prev[0]) > 1:  # Breek keten
                    chains.append(corrected_chain)
                    corrected_chain = []

            corrected_chain.append(current)
            idx += 1

        # Voeg de laatste keten toe
        if corrected_chain:
            chains.append(corrected_chain)


    return chains


for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j][1]:
            continue
        else:
            area, area_grid = calc(i,j)
            perimeter_parts = calculate_connections(list(set(sorted(flatten_list(area_grid)))))
            total_price += area * len(perimeter_parts)
            print("area_grid: ", area_grid)
            print(f" ({i},{j}): {grid[i][j]}, area: {area}, perim-len: {len(perimeter_parts)}, perim: {perimeter_parts}")


print(f"Part 2: {total_price}")
