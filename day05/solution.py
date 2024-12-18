orderings = {}
updates = []

with open('input.txt') as file:
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
    try:
        orderingspage = orderings[page]
    except KeyError:
        return True
    for tocheck in orderingspage:
        if tocheck in update:
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
                # sla de index van de te veranderen page op
                indexoftocheck = update.index(tocheck)
                # Verwijder de te veranderen page
                update.remove(tocheck)
                # insert de te veranderen page een plek na waar het nu stond
                inserAfter(update, indexoftocheck, tocheck)
                # print("after ",update)

    return update

def inserAfter(update, indexoftocheck, tocheck):
    flag = False
    for newindex in range(1, len(update) - indexoftocheck):
        checkIfValid = update.copy()
        checkIfValid.insert(indexoftocheck + newindex, tocheck)
        if checkIfAfter(indexoftocheck + newindex, update, orderings):
            update.insert(indexoftocheck + newindex, tocheck)
            flag = True
            break
    if not flag:
            update.append(tocheck)
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
                    replace = part2({updatenr:update})
                    for rk, rv in replace:
                        invalids[rk] = rv
                        valids[rk] += 1
            else:
                valids[updatenr] += 1
    return [ (index, updates[index])  for index, length in valids.items() if len(updates[index]) == length]

print(calculatemid(part1()[0]))
print("---------------------------")
print(calculatemid(part2(part1()[1])))