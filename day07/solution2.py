with open("input.txt", "r") as f:
    result = 0
    for line in f:
        tree = []
        a, qs = line.strip("\n").split(":")
        answer = int(a)
        questions = qs.strip().split()

        for idx, q in enumerate(questions):
            if idx == 0:
                tree.append([int(q)])
            else:
                tree.append([])
                for prev in tree[idx-1]:
                    tree[idx].append(prev*int(q))
                    tree[idx].append(prev+int(q))
            # print(tree)
        if answer in tree[len(questions)-1]:
            print(f"Answer {answer} gevonden")
            result += answer
    print(f"Part 1 {result=}")