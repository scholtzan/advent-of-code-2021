# part 1
with open("input-day12.txt") as input:
    graph = {}
    for line in input:
        line = line.replace("\n", "")
        [start, end] = line.split("-")

        if start in graph:
            graph[start] += [end]
        else:
            graph[start] = [end]

        if end in graph:
            graph[end] += [start]
        else:
            graph[end] = [start]

    def total_paths(node, visited = []):
        if node == "end":
            return 1

        if node.lower() != node or node not in visited:
            visited += [node]
            return sum([total_paths(n, visited.copy()) for n in graph[node]])
        else:
            return 0

    print(total_paths("start"))

# part 2
with open("input-day12.txt") as input:
    graph = {}
    for line in input:
        line = line.replace("\n", "")
        [start, end] = line.split("-")

        if start in graph:
            graph[start] += [end]
        else:
            graph[start] = [end]

        if end in graph:
            graph[end] += [start]
        else:
            graph[end] = [start]

    def total_paths(node, visited = [], twiced = False):
        if node == "end":
            return 1

        if node.lower() != node or node not in visited or twiced is False:
            visited += [node]
            if node.lower() == node and visited.count(node) >= 2:
                twiced = True

            return sum([total_paths(n, visited.copy(), twiced) for n in graph[node] if n != "start"])
        else:
            return 0

    print(total_paths("start"))