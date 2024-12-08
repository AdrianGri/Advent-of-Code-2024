from collections import defaultdict, deque

def solution():
    str = open('input.txt').read().split("\n")

    edges = defaultdict(set)

    orderings = []

    for line in str:
        if "|" in line:
            first, second = line.split("|")
            edges[first].add(second)
        elif "," in line:
            pages = line.split(",")
            orderings.append(pages)
    
    invalid_orderings = []

    for ordering in orderings:
        valid = True
        for i in range(len(ordering)):
            for j in range(i + 1, len(ordering)):
                if ordering[j] not in edges[ordering[i]]:
                    valid = False
                    break
            if not valid:
                break
        
        if not valid:
            invalid_orderings.append(ordering)
    
    res = 0
    for ordering in invalid_orderings:
        nodes = set(ordering)
        indeg = defaultdict(int)
        next = defaultdict(set)

        for node in nodes:
            for other_node in edges[node]:
                if other_node in nodes:
                    next[node].add(other_node)
                    indeg[other_node] += 1
        
        order = []
        q = deque([node for node in nodes if indeg[node] == 0])

        while len(q):
            cur = q.popleft()
            order.append(cur)

            for node in next[cur]:
                indeg[node] -= 1

                if indeg[node] == 0:
                    q.append(node)
        
        res += int(order[len(order) // 2])
    
    return res

print(solution())