# part 1
with open("input-day13.txt") as input:
    coordinates = []
    folds = []
    for line in input:
        line = line.replace("\n", "")

        if line == "":
            continue
        elif line.startswith("fold"):
            line = line.replace("fold along ", "")
            [axis, i] = line.split("=")
            folds.append([axis == 'x', int(i)])
        else:
            coordinates.append([int(i) for i in line.split(",")])

    def fold(i, is_x = True):
        new_coordinates = []
        axis = 0 if is_x else 1
        for c in coordinates:
            if c[axis] < i:
                if c not in new_coordinates:
                    new_coordinates.append(c)
            else:
                c[axis] = i - (c[axis] - i)
                if c not in new_coordinates:
                    new_coordinates.append(c)

        return new_coordinates

    for f in folds:
        coordinates = fold(f[1], f[0])
        print(len(coordinates))

    # part 2
    max_x = 0
    max_y = 0

    for c in coordinates:
        if c[0] > max_x:
            max_x = c[0]
        if c[1] > max_y:
            max_y = c[1]

    for y in range(0, max_y + 1):
        for x in range(0, max_x + 1):
            if [x, y] not in coordinates:
                print(" ", end="")
            else:
                print("#", end="")

            if x == max_x:
                print("")

    # RGZLBHFP
