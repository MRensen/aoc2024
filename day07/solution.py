import sys

total = 0
SUM = True
MULT = False


# check of het eerste getal + 0 en * 0
# check dan of het tweede getal plus de uitkomst kan
# check dan of het derde getal plus de uitkomst kan
# ....etc
# Elke keer 2 berekeningen
# Als er eentje groter is dan het beoogde antwoord, dan return None
def equate(index, parts, expected, cum):
    result = cum

    # Als de index te out of scope van parts is, gaan we niet verder
    if index > len(parts)-1:
        if cum != expected:
            return None
        else:
            print(f"returning: {cum}")
            return cum
    # als het goed is is het goed
    if cum==expected:
        return cum

    sumans = cum + int(parts[index])
    multans = cum * int(parts[index])

    print(f"{expected}:{parts}[{index}] -> sum:{sumans} - mult:{multans}")

    if sumans == expected:
        result = sumans
    if multans == expected:
        result = multans
        if(sumans == expected):
            print(f"allebij zijn ze expected: {expected } : {parts}", file=sys.stderr)
    if sumans < expected:
        result = equate(index=index+1, parts=parts, expected=expected, cum=sumans)
    if multans < expected:
        result = equate(index=index+1, parts=parts, expected=expected, cum=multans)

    return result


with open("test.txt", "r") as f:
    result = 0
    for line in f:
        answer, qs = line.strip("\n").split(":")
        answer = int(answer)
        questions = qs.strip().split()
        sumresult = equate(index=0, parts=questions, expected=answer, cum=0)
        multresult = equate(0, questions, answer, SUM)
        if multresult == None and sumresult == None:
            print("Allebij fout", file=sys.stderr)
        elif multresult != None:
            result += multresult
        else:
            result += sumresult
        print(f"Part 1 = {result}")


