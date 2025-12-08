running_total = 0
lines = []

with open("test_input.txt") as file:
    for line in file:
        lines.append(line.strip())

for i in range(1,len(lines)):
    for j in range(len(lines[i])):
        if lines[i-1][j] == 'S':
            temp_line = list(lines[i])
            temp_line[j] = "|"
            lines[i] = "".join(temp_line)
        if lines[i][j] == '^' and lines[i-1][j] == '|':
            temp_line = list(lines[i])
            temp_line[j-1] = "|"
            temp_line[j+1] = "|"
            lines[i] = "".join(temp_line)
            running_total += 1
        if lines[i][j] == "." and lines[i-1][j] == '|':
            temp_line = list(lines[i])
            temp_line[j] = lines[i-1][j]
            lines[i] = "".join(temp_line)

print(*lines, sep='\n')
print(running_total)
