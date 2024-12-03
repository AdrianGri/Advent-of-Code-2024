def is_safe(levels):
    inc = int(levels[0]) < int(levels[1])
            
    for i in range(len(levels) - 1):
        first, second = int(levels[i]), int(levels[i + 1])
        diff = abs(first - second)
        is_inc = first < second

        if diff < 1 or diff > 3:
            break
        if is_inc != inc:
            break
    else:
        return True
    return False

def solution():
    reports = open("input.txt").read().split("\n")

    safe_count = 0

    for report in reports:
        levels = report.split(" ")
            
        if is_safe(levels):
            safe_count += 1
            continue

        for i in range(len(levels)):
            if is_safe(levels[:i] + levels[i + 1:]):
                safe_count += 1
                break
    
    return safe_count
            
print(solution())