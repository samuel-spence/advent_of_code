running_total = 0
good_ids = list()
temp_ids = None
start = 0
end = 0

with open("input.txt", "r") as f:
    for line in f:
        if "-" in line:
            nums = line.split("-")
            start = int(nums[0])
            end = int(nums[1])
            good_ids.append(range(start, end + 1))
    sorted_ids = sorted(good_ids, key=lambda r: r.start)
    for index, ids in enumerate(sorted_ids):
        if index == 0:
            start = ids[0]
            end = ids[-1]
        if index < len(sorted_ids) - 1 and end >= sorted_ids[index + 1][0]:
            end = max(end, sorted_ids[index + 1][-1])
            continue
        running_total += len(range(start, end + 1))
        if index < len(sorted_ids) - 1:
            start = sorted_ids[index + 1][0]
            end = sorted_ids[index + 1][-1]
    print(running_total)
