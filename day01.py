# part 1
with open("input-day01.txt") as input:
    prev = None
    increases = 0
    for i in input:
        current = int(i)
        if prev is not None and prev < current:
            increases += 1
        prev = current

print(increases)


# part 2
with open("input-day01.txt") as input:
    measurements = [int(i) for i in input]

    prev = sum(measurements[0:3])
    current = 0
    increases = 0

    for i in range(3, len(measurements)):
        current = prev - measurements[i-3] + measurements[i]

        if prev < current:
            increases += 1
        prev = current

print(increases)
