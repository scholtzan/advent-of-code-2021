# part 1

def n_babies(timer, days):
    days_left = days - timer - 1
    babies = 0

    if days_left < 0:
        return babies

    for d in range(0, (days_left // 7) + 1):
        babies += n_babies(8, days_left - d * 7) + 1

    return babies

with open("input-day06.txt") as input:
    fish = [int(t) for t in list(input)[0].split(",")]

    print(sum([n_babies(t, 80) + 1 for t in fish]))


# part 2
with open("input-day06.txt") as input:
    days = 256
    fish = [int(t) for t in list(input)[0].split(",")]
    timers = [0] * 9

    for f in fish:
        timers[f] += 1

    for day in range(0, days):
        timers = timers[1:] + [timers[0]]
        timers[6] += timers[8]

    print(sum(timers))
