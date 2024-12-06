from collections import deque

def solution():
    grid = open("input.txt").read().split("\n")
    ROWS, COLS = len(grid), len(grid[0])

    corners = [[-1, -1], [-1, 1], [1, 1], [1, -1]]

    res = 0
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] != "A":
                continue
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                continue

            for corner_index in range(len(corners)):
                next_corner_index = (corner_index + 1) % len(corners)
                
                d1r, d1c = corners[corner_index]
                d2r, d2c = corners[next_corner_index]

                if grid[r + d1r][c + d1c] != "M" or grid[r + d2r][c + d2c] != "M":
                    continue
                    
                corner_index_mapping = (corner_index + 2) % len(corners)
                next_corner_index_mapping = (next_corner_index + 2) % len(corners)

                c1r, c1c = corners[corner_index_mapping]
                c2r, c2c = corners[next_corner_index_mapping]

                if grid[r + c1r][c + c1c] != "S" or grid[r + c2r][c + c2c] != "S":
                    continue
                    
                res += 1

    return res

print(solution())