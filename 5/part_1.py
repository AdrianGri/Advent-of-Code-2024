from collections import defaultdict

def solution():
    str = open('input.txt').read().split("\n")

    edges = set()

    orderings = []

    for line in str:
        if "|" in line:
            first, second = line.split("|")
            edges.add((first, second))
        elif "," in line:
            pages = line.split(",")
            orderings.append(pages)
    
    valid_orderings = []

    for ordering in orderings:
        valid = True
        for i in range(len(ordering)):
            for j in range(i + 1, len(ordering)):
                if (ordering[i], ordering[j]) not in edges:
                    valid = False
                    break
            if not valid:
                break
        else:
            valid_orderings.append(ordering)
    
    res = 0
    for ordering in valid_orderings:
        res += int(ordering[len(ordering) // 2])
    
    return res

print(solution())