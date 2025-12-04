current_position = 50
target = 50
total_zeros = 0

def rotate_dial(tgt, num_zeros = 0):
    if 0 < tgt < 100:
        return tgt, num_zeros
    if tgt == 0 or tgt == 100:
        return 0, num_zeros + 1
    if direction == "R":
        tgt -= 100
    if direction == "L":
        tgt += 100
    return rotate_dial(tgt, num_zeros + 1)


with open("input.txt", "r") as f:
    for line in f:
        print(f"{current_position}->{line.strip()}->", end="")
        direction = line[0]
        amount = int(line[1:].strip())
        if current_position == 0 and direction == "L":
            current_position = 100
        if direction == "R":
            target = current_position + amount
        if direction == "L":
            target = current_position - amount
        current_position, count = rotate_dial(target)
        total_zeros += count
        print(f"{current_position} -- {total_zeros}")
    print(f"{total_zeros}")

