running_total = 0
lines = []

with open("input.txt") as file:
    for line in file:
        lines.append(line.strip())

def move_beam(col, row, total=0):
    if row == len(lines)-1:
        return 1
    while lines[row+1][col] == ".":
        row += 1
        if row == len(lines)-1:
            return 1
    if lines[row+1][col] == "^":
        return move_beam(col-1, row+1, total) + move_beam(col+1, row+1, total)

column = lines[0].index('S')

print(move_beam(column, 1))
