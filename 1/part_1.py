def solution():
    vals = open("input.txt").read().split("\n")

    one, two = [], []

    for v in vals:
        o, t = v.split("   ")
        one.append(int(o))
        two.append(int(t))

    one = sorted(one)
    two = sorted(two)

    diff = 0
    for i in range(len(one)):
        if one[i] != two[i]:
            diff += abs(one[i] - two[i])
    
    return diff

print(solution())