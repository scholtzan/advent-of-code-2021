# part 1
with open("input-day09.txt") as input:
    profile = []
    for line in input:
        profile.append([int(i) for i in line.replace("\n", "")])

    risk_level = 0

    for x in range(0, len(profile)):
        for y in range(0, len(profile[x])):
            adjacent = []
            if x - 1 >= 0:
                adjacent.append(profile[x-1][y])
            if x + 1 < len(profile):
                adjacent.append(profile[x+1][y])
            if y - 1 >= 0:
                adjacent.append(profile[x][y-1])
            if y + 1 < len(profile[x]):
                adjacent.append(profile[x][y+1])

            if all([a > profile[x][y] for a in adjacent]):
                risk_level += profile[x][y] + 1

    print(risk_level)


# part 2
import math

with open("input-day09.txt") as input:
    profile = []
    for line in input:
        profile.append([int(i) for i in line.replace("\n", "")])

    def basin_size(pos, seen):
        size = 0
        if pos not in seen:
            size += 1
            seen.append(pos)
        else:
            return size

        (x, y) = pos

        if x - 1 >= 0 and profile[x-1][y] != 9:
            size += basin_size((x-1, y), seen)
        if x + 1 < len(profile) and profile[x+1][y] != 9:
            size += basin_size((x+1, y), seen)
        if y - 1 >= 0 and profile[x][y-1] != 9:
            size += basin_size((x, y-1), seen)
        if y + 1 < len(profile[x]) and profile[x][y+1] != 9:
            size += basin_size((x, y+1), seen)

        return size

    basins = []
    for x in range(0, len(profile)):
        for y in range(0, len(profile[x])):
            adjacent = []
            if x - 1 >= 0:
                adjacent.append(profile[x-1][y])
            if x + 1 < len(profile):
                adjacent.append(profile[x+1][y])
            if y - 1 >= 0:
                adjacent.append(profile[x][y-1])
            if y + 1 < len(profile[x]):
                adjacent.append(profile[x][y+1])

            if all([a > profile[x][y] for a in adjacent]):
                basins.append(basin_size((x, y), []))

    print(math.prod(sorted(basins)[-3:]))