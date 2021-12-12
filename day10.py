# part 1
points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

mapping = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

with open("input-day10.txt") as input:
    score = 0
    for line in input:
        stack = []
        line = line.replace("\n", "")

        for c in line:
            if c in mapping.keys():
                stack.append(c)
            else:
                if mapping[stack[-1]] != c:
                    score += points[c]
                    break
                else:
                    stack = stack[:-1]

    print(score)

# part 2
compl_points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

with open("input-day10.txt") as input:
    scores = []
    for line in input:
        stack = []
        line = line.replace("\n", "")
        invalid = False

        for c in line:
            if c in mapping.keys():
                stack.append(c)
            else:
                if mapping[stack[-1]] != c:
                    invalid = True
                    break
                else:
                    stack = stack[:-1]

        if not invalid and len(stack) > 0:
            score = 0
            for s in reversed(stack):
                score *= 5
                score += compl_points[mapping[s]]
            scores.append(score)

    print(sorted(scores)[int(len(scores) / 2)])
