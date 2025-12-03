running_total = 0

def find_largest_digit(num, size, result=''):
    if size == 0:
        temp_num = num
    else:
        temp_num = num[:-size]
    largest_digit = max(temp_num)
    index = num.index(largest_digit)
    result += largest_digit
    if size > 0:
        return find_largest_digit(num[index+1:], size -1, result)
    return result

with open('input.txt', 'r') as file:
    for line in file:
        line = line.strip()
        length = len(line)
        res = find_largest_digit(line, 11)
        print(res)
        running_total += int(res)
    print(running_total)
