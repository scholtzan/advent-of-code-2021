# part 1
with open("input-day05.txt") as input:
    coordinates = {}

    for line in input:
        parts = line.split(" -> ")
        [x0, y0] = [int(n) for n in parts[0].split(",")]
        [x1, y1] = [int(n) for n in parts[1].split(",")]

        if x0 == x1 or y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y1, y0) + 1):
                    if (x, y) in coordinates:
                        coordinates[(x, y)] += 1
                    else:
                        coordinates[(x, y)] = 1

    print(len([n for n in coordinates.values() if n >= 2]))

# part 2
with open("input-day05.txt") as input:
    coordinates = {}

    for line in input:
        parts = line.split(" -> ")
        [x0, y0] = [int(n) for n in parts[0].split(",")]
        [x1, y1] = [int(n) for n in parts[1].split(",")]

        offset = 0
        for x in range(min(x0, x1), max(x0, x1) + 1):
            for y in range(min(y0, y1), max(y1, y0) + 1):
                if x1 != x0 and y0 != y1:
                    if ((y != y0 + offset and x0 < x1 and y0 < y1) or 
                        (y != y1 - offset and x1 < x0 and y0 < y1) or
                        (y != y1 + offset and x1 < x0 and y0 > y1) or
                        (y != y0 - offset and x1 > x0 and y0 > y1)):
                        continue

                if (x, y) in coordinates:
                    coordinates[(x, y)] += 1
                else:
                    coordinates[(x, y)] = 1

            if x1 != x0 and y0 != y1:
                offset += 1

    print(len([n for n in coordinates.values() if n >= 2]))