from collections import defaultdict

def solution():
    vals = open("input.txt").read().split("\n")

    one, two = [], []

    for v in vals:
        o, t = v.split("   ")
        one.append(int(o))
        two.append(int(t))

    similarity = 0
    occ = defaultdict(int)
    
    for n in two:
        occ[n] += 1

    for n in one:
        similarity += n * occ[n]

    return similarity

print(solution())