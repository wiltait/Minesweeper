from pprint import pprint

mines = [
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "#", "-"],
    ["-", "-", "#", "#", "-"],
    ["#", "-", "-", "-", "-"],
    ["-", "-", "#", "#", "-"]
]

def minesweeper(mines):
    
    # Solution grid
    n = 5
    arr = [[0 for r in range(n)] for c in range(n)]

    for row, rval in enumerate(mines):
        for col, value in enumerate(mines[row]):            
            
            # Place the bombs in the solution grid
            if value == "#":
               arr[row][col] = "#"

            # Center
            if (1 <= row <= 3) and (1 <= col <= 3):
                if value == "#":
                    if arr[row-1][col] != "#": arr[row-1][col] += 1
                    if arr[row+1][col] != "#": arr[row+1][col] += 1
                    if arr[row][col+1] != "#": arr[row][col+1] += 1
                    if arr[row][col-1] != "#": arr[row][col-1]+= 1
                    if arr[row-1][col-1] != "#": arr[row-1][col-1] += 1
                    if arr[row+1][col-1] != "#": arr[row+1][col-1] += 1
                    if arr[row-1][col+1] != "#": arr[row-1][col+1] += 1
                    if arr[row+1][col+1] != "#": arr[row+1][col+1] += 1

            # Top left corner
            if row == 0 and col == 0:
                if value == "#":
                    if arr[row+1][col] != "#": arr[row+1][col] += 1
                    if arr[row][col+1] != "#": arr[row][col+1] += 1
                    if arr[row+1][col+1] != "#": arr[row+1][col+1] += 1
                           
            # Top right corner
            if row == 0 and col == 4:
                if value == "#":
                    if arr[row][col-1] != "#": arr[row][col-1] += 1
                    if arr[row+1][col] != "#": arr[row+1][col] += 1
                    if arr[row+1][col-1] != "#": arr[row+1][col-1] += 1
            
            # Bottom left corner
            if row == 4 and col == 0:
                if value == "#":
                    if arr[row-1][col] != "#": arr[row-1][col] += 1
                    if arr[row][col+1] != "#": arr[row][col+1] += 1
                    if arr[row-1][col+1] != "#": arr[row-1][col+1] += 1

            # Bottom right corner
            if row == 4 and col == 4:
                if value == "#":
                    if arr[row-1][col] != "#": arr[row-1][col] += 1
                    if arr[row][col-1] != "#": arr[row][col-1] += 1
                    if arr[row-1][col-1] != "#": arr[row-1][col-1] += 1

            # Left border
            if (1 <= row <= 3) and col == 0:
                if value == "#":
                    if arr[row-1][col] != "#": arr[row-1][col] += 1
                    if arr[row+1][col] != "#": arr[row+1][col] += 1
                    if arr[row][col+1] != "#": arr[row][col+1] += 1
                    if arr[row-1][col+1] != "#": arr[row-1][col+1] += 1
                    if arr[row+1][col+1] != "#": arr[row+1][col+1] += 1

            # Right border
            if (1 <= row <= 3) and col == 4:
                if value == "#":
                    if arr[row-1][col] != "#": arr[row-1][col] += 1
                    if arr[row+1][col] != "#": arr[row+1][col] += 1
                    if arr[row][col-1] != "#": arr[row][col-1] += 1
                    if arr[row-1][col-1] != "#": arr[row-1][col-1] += 1
                    if arr[row+1][col-1] != "#": arr[row+1][col-1] += 1

            # Top border
            if row == 0 and (1 <= col <= 3):
                if value == "#":
                    if arr[row][col-1] != "#": arr[row][col-1] += 1
                    if arr[row][col+1] != "#": arr[row][col+1] += 1
                    if arr[row+1][col] != "#": arr[row+1][col] += 1
                    if arr[row+1][col-1] != "#": arr[row+1][col-1] += 1
                    if arr[row+1][col+1] != "#": arr[row+1][col+1] += 1
            
            # Bottom border
            if row == 4 and (1 <= col <= 3):
                if value == "#":
                    if arr[row][col-1] != "#": arr[row][col-1] += 1
                    if arr[row][col+1] != "#": arr[row][col+1] += 1
                    if arr[row-1][col] != "#": arr[row-1][col] += 1
                    if arr[row-1][col-1] != "#": arr[row-1][col-1] += 1
                    if arr[row-1][col+1] != "#": arr[row-1][col+1] += 1

    pprint(arr)

output = minesweeper(mines=mines)