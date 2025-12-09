with open("input.txt", "r") as file:
    lines = file.read().splitlines()

points = list()
for line in lines:
    x, y = line.split(',')
    points.append([int(x), int(y)])

areas = list()

for index, point in enumerate(points):
    x, y = points[index]
    for i in range(index+1, len(points)):
        x1, y1 = points[i]
        diff_x = abs(x1 - x) + 1
        diff_y = abs(y1 - y) + 1
        areas.append(diff_x * diff_y)

print(max(areas))
