# part 1
with open("input-day14.txt") as input:
    template = None
    rules = {}
    for line in input:
        line = line.replace("\n", "")
        if line != "":
            if template is None:
                template = line
            else:
                [insert, out] = line.split(" -> ")
                rules[insert] = out

    total_steps = 10
    for step in range(0, total_steps):
        print(step)
        new_template = template[0]
        for i in range(0, len(template) - 1):
            pair = template[i:i+2]
            if pair in rules:
                new_template += rules[pair]
            
            new_template += template[i+1]

        template = new_template

    most_common = template.count(max(set(template), key=template.count))
    least_common = template.count(min(set(template), key=template.count))
    print(most_common - least_common)

# part 2
import copy

with open("input-day14.txt") as input:
    template = None
    rules = {}
    for line in input:
        line = line.replace("\n", "")
        if line != "":
            if template is None:
                template = line
            else:
                [insert, out] = line.split(" -> ")
                rules[insert] = out

    cache = {}
    for i in range(0, len(template) - 1):
        pair = template[i:i+2]
        if pair not in cache:
            cache[pair] = 0
        cache[pair] += 1

    total_steps = 40
    for step in range(0, total_steps):
        print(step)
        temp = {}

        for key, v in cache.items():
            if key[0] + rules[key] not in temp:
                temp[key[0] + rules[key]] = 0

            temp[key[0] + rules[key]] += v

            if rules[key] + key[1] not in temp:
                temp[rules[key] + key[1]] = 0
            temp[rules[key] + key[1]] += v
            cache = copy.deepcopy(temp)

    counts = {}
    c = []
    for key, val in cache.items():
        v1, v2 = key[0], key[1]
        if v1 not in counts:
            counts[v1] = 0
        counts[v1] += val

        if v2 not in counts:
            counts[v2] = 0
        counts[v2] += val
    
    for key, val in counts.items():
        if key == template[0] or key == template[1]:
            counts[key] = int((val - 1) / 2)
            c += [counts[key]]
        else:
            counts[key] = int(counts[key] / 2)
            c += [counts[key]]

    c.sort()
    print(c[-1] - c[0] + 1)
