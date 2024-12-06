import re

def solution():
    str = open("input.txt").read()

    starts = [m.start() for m in re.finditer(r"mul\([\d]{1,3},[\d]{1,3}\)", str)]

    res = 0
    for start in starts:
        multipliers = str[start+4:start+12]

        comma_splits = multipliers.split(",")
        first = comma_splits[0]
        paren_splits = comma_splits[1].split(")")
        second = paren_splits[0]

        res += int(first) * int(second)

    return res

print(solution())