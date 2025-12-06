lines = []
running_total = 0
with open('input.txt', 'r') as f:
    for line in f:
        lines.append(line.replace("\n", " "))
operators = lines[len(lines) - 1].split()
temp_nums = []
new_lines = []

for i in range(len(lines[0])):
    temp_num = []
    for j in range(len(lines)-1):
        temp_num.append(lines[j][i])
    if "".join(temp_num).strip() == "" :
        new_lines.append(temp_nums)
        temp_nums = []
        continue
    if len("".join(temp_num).strip()) > 0:
        temp_nums.append("".join(temp_num).strip())

for i in range(len(new_lines)):
    problem = operators[i].join(new_lines[i])
    print(problem)
    running_total += eval(problem)
print(running_total)
