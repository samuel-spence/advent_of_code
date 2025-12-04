def move_rolls(data, total=0):
    temp_data = data.copy()
    temp_total = 0
    for row in range(0, len(data)):
        for col in range(0, len(data[row])):
            if data[row][col] == '@':
                num_rolls = 0
                for i in range(row -1, row + 2):
                    for j in range(col -1, col + 2):
                        if i < 0 or i >= len(data):
                            continue
                        if j < 0 or j >= len(data[i]):
                            continue
                        if i == row and j == col:
                            continue
                        if data[i][j] == '@':
                            num_rolls += 1
                if num_rolls < 4:
                    temp_total += 1
                    temp_list = list(temp_data[row])
                    temp_list[col] = 'x'
                    temp_str = ''.join(temp_list)
                    temp_data[row] = temp_str
    if temp_total > 0:
        return move_rolls(temp_data, total + temp_total)
    return total


with open('input.txt', 'r') as file:
    grid = list()
    for line in file:
        grid.append(line.strip())
    running_total = move_rolls(grid)
    print(running_total)

