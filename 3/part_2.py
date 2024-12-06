import re

def solution():
    str = open("input.txt").read()

    mul_starts = [m.start() for m in re.finditer(r"mul\([\d]{1,3},[\d]{1,3}\)", str)]
    do_starts = [m.start() for m in re.finditer(r"do\(\)", str)]
    dont_starts = [m.start() for m in re.finditer(r"don't\(\)", str)]

    all_starts = []

    for start in mul_starts:
        all_starts.append((start, "mul"))
    for start in do_starts:
        all_starts.append((start, "do"))
    for start in dont_starts:
        all_starts.append((start, "dont"))

    all_starts.sort()

    res = 0
    enabled = True
    for start, command in all_starts:
        if command == "do":
            enabled = True
        elif command == "dont":
            enabled = False
        elif enabled:
            multipliers = str[start+4:start+12]

            comma_splits = multipliers.split(",")
            first = comma_splits[0]
            paren_splits = comma_splits[1].split(")")
            second = paren_splits[0]

            res += int(first) * int(second)

    return res

print(solution())