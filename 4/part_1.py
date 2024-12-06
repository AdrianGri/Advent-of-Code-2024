from collections import deque

def solution():
    grid = open("input.txt").read().split("\n")
    ROWS, COLS = len(grid), len(grid[0])

    next_char = { "X": "M", "M": "A", "A": "S" }
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    q = deque()

    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == "X":
                for dr, dc in dirs:
                    q.append((row, col, dr, dc))


    res = 0
    while len(q):
        r, c, dr, dc = q.popleft()
        if grid[r][c] == "S":
            res += 1
            continue

        nr, nc = r + dr, c + dc

        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
            continue

        if grid[nr][nc] == next_char[grid[r][c]]:
            q.append((nr, nc, dr, dc))
    
    return res

print(solution())