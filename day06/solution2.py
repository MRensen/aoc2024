from itertools import cycle

guard_cur = ()
obstacles = []
guard_his = []
len_map = 0

dirs_pos = {'s': (1, 0), 'n': (-1, 0), 'w': (0, -1),'e': (0, 1)}  # welke bewegingen gedaan moeten worden voor elke windricthing
dirs = cycle(['n', 'e', 's', 'w'])  # Wrapping iterator voor alle windrichtingen
dir_cur = dirs.__next__()

loops = 0


with open("test.txt") as f:
    for x, line in enumerate(f):
        len_map = len(line)
        for y, char in enumerate(line.strip()):
            if char == '^':
                guard_cur = (x, y)
            if char == '#':
                obstacles.append((x, y))

def walk(obstacles):
    global guard_cur, dir_cur
    keep_going = True
    while keep_going:
        new_pos = (guard_cur[0] + dirs_pos[dir_cur][0], guard_cur[1] + dirs_pos[dir_cur][1])

        #End if you reach the limit of the map
        if new_pos[0] < 0 or new_pos[0] >= len_map or new_pos[1] < 0 or new_pos[1] >= len_map:
            keep_going = False
            continue

        # move until you reach an obstacle
        if new_pos not in obstacles:
            guard_cur = new_pos
            guard_his.append((new_pos[0], new_pos[1], dir_cur))

        # if you reach an obstacle, turn and start moving again
        else:
            dir_cur = dirs.__next__()
            walk(obstacles)
            keep_going = False


def part2(guard_his2, obstacles2):
    global guard_cur, dir_cur
    keep_going = True
    while keep_going:
        new_pos = (guard_cur[0] + dirs_pos[dir_cur][0], guard_cur[1] + dirs_pos[dir_cur][1])

        # End if you reach the limit of the map
        if new_pos[0] < 0 or new_pos[0] >= len_map or new_pos[1] < 0 or new_pos[1] >= len_map:
            keep_going = False
            continue

        if (new_pos[0], new_pos[1], dir_cur) in guard_his2:
            global loops
            loops += 1
            print(new_pos, dir_cur)
            print(guard_his2)
            return  #loop


        # move until you reach an obstacle
        if new_pos not in obstacles:
            guard_cur = new_pos
            obstacles2.append(new_pos)
            part2(guard_his2, obstacles2)
            obstacles2.remove(new_pos)
            guard_his2.append((new_pos[0], new_pos[1], dir_cur))

        # if you reach an obstacle, turn and start moving again
        else:
            dir_cur = dirs.__next__()
            walk(obstacles2)
            keep_going = False


    return  #no loop



walk(obstacles)
print("The answer to part 1 = ", len(set(guard_his)))
#reset
dirs = cycle(['n', 'e', 's', 'w'])
dir_cur = dirs.__next__()

#part2
part2(guard_his, obstacles)
print(loops)
