orderings = {}
updates = []

with open('test.txt') as file:
    switch = False
    for line in file:
        if line == '\n':
            switch = True
            continue
        if switch:
            updates.append([int(i) for i in list(line.strip().split(","))])
        else:
            x,y = line.split('|')
            if int(x) in orderings.keys():
                orderings[int(x)].append(int(y.strip()))
            else:
                orderings[int(x)] = [int(y.strip())]
print("udate: ",updates)
print("order: ",orderings)


def checkIfAfter(index, update, orderings):
    page = update[index]
    orderingspage = orderings[page]
    for tocheck in orderingspage:
        if tocheck in update:
        #     for postpage in range(len(update)-1):
        #         updatepostpage = update[0+postpage::]
        #         if tocheck in updatepostpage:
        #             continue
        #         else:
        #             return False
        # else:
        #     return False
            update.index(page)
            if tocheck in update[:update.index(page):]:
                return False

    return True

def fixafter(index, update:list, orderings):
    page = update[index]
    orderingspage = orderings[page]
    for tocheck in orderingspage:
        if tocheck in update:
            if tocheck in update[:update.index(page):]:
                # print("before",update)
                indexoftecheck = update.index(tocheck)
                update.remove(tocheck)
                # update.insert(update.index(page)+1 if update.index(page)+1 < len(update)-1 else update.index(page), tocheck)
                update.insert(indexoftecheck+1, tocheck)
                # print("after ",update)

    return update


def part1():
    valids = {}
    invalids = {}

    for updatenr, update in enumerate(updates):
        valids[updatenr] = 0
        for index, page in enumerate(update):
            if page in orderings.keys():
                valid = checkIfAfter(index, update, orderings)
                if valid:
                    valids[updatenr] += 1
                else:
                    invalids[updatenr]= update
            else:
                valids[updatenr] += 1
    # return [(nr, updates[nr]) for nr in valids]
    # print(valids)
    # print(set([str(inv) for inv in invalids]))
    print(invalids)
    return [ (index, updates[index])  for index, length in valids.items() if len(updates[index]) == length], invalids


def calculatemid(partlist):
    count = 0
    for _, update in partlist:
        count += update[int(len(update)/2)]
    return count



def part2(invalids):
    valids = {}

    for updatenr, update in invalids.items():
        valids[updatenr] = 0
        for index, page in enumerate(update):
            if page in orderings.keys():
                valid = checkIfAfter(index, update, orderings)
                if valid:
                    valids[updatenr] += 1
                else:
                    update = fixafter(index, update, orderings)
                    part2({updatenr:update})
                    # for rk, rv in part2({updatenr: update}):
                        # print("for")
                        # valids[rk] += rv
            else:
                valids[updatenr] += 1
    # print(valids)
    return [ (index, updates[index])  for index, length in valids.items() if len(updates[index]) == length]

print(calculatemid(part1()[0]))
print("---------------------------")
print(calculatemid(part2(part1()[1])))