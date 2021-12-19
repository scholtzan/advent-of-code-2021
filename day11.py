# part 1
with open("input-day11.txt") as input:
    energy = []
    for line in input:
        line = line.replace("\n", "")
        energy.append([int(e) for e in line])

    total_flashes = 0

    def update_neighbors(x, y):
        flashes = 0
        for d_x in range(-1, 2):
            for d_y in range(-1, 2):
                if not(d_x == 0 and d_y == 0):
                    if x + d_x >= 0 and x + d_x < len(energy) and y + d_y >= 0 and y + d_y < len(energy[x]):
                        if energy[x + d_x][y + d_y] != 0:
                            energy[x + d_x][y + d_y] += 1

                            if energy[x + d_x][y + d_y] > 9:
                                energy[x + d_x][y + d_y] = 0
                                flashes += 1
                                flashes += update_neighbors(x + d_x, y + d_y)

        return flashes

    for step in range(0, 100):
        for x in range(0, len(energy)):
            for y in range(0, len(energy[x])):
                energy[x][y] += 1


        for x in range(0, len(energy)):
            for y in range(0, len(energy[x])):
                if energy[x][y] > 9:
                    total_flashes += 1
                    energy[x][y] = 0
                    total_flashes += update_neighbors(x, y)


    print(total_flashes)


# part 2
with open("input-day11.txt") as input:
    energy = []
    for line in input:
        line = line.replace("\n", "")
        energy.append([int(e) for e in line])

    total_flashes = 0

    def update_neighbors(x, y):
        flashes = 0
        for d_x in range(-1, 2):
            for d_y in range(-1, 2):
                if not(d_x == 0 and d_y == 0):
                    if x + d_x >= 0 and x + d_x < len(energy) and y + d_y >= 0 and y + d_y < len(energy[x]):
                        if energy[x + d_x][y + d_y] != 0:
                            energy[x + d_x][y + d_y] += 1

                            if energy[x + d_x][y + d_y] > 9:
                                energy[x + d_x][y + d_y] = 0
                                flashes += 1
                                flashes += update_neighbors(x + d_x, y + d_y)

        return flashes

    step = 0
    found = False
    while not found:
        step += 1
        for x in range(0, len(energy)):
            for y in range(0, len(energy[x])):
                energy[x][y] += 1


        for x in range(0, len(energy)):
            for y in range(0, len(energy[x])):
                if energy[x][y] > 9:
                    total_flashes += 1
                    energy[x][y] = 0
                    total_flashes += update_neighbors(x, y)

        if all([y == 0 for x in energy for y in x]):
            found = True

    print(step)