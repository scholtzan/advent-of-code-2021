# part 1
class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.risk = 0
        self.total_risk = 0
        self.risk_to_end = 0
        self.risk_to_start = 0

    def __eq__(self, other):
        return self.position == other.position

with open("input-day15.txt") as input:
    maze = []
    for line in input:
        line = line.replace("\n", "")
        maze.append([int(i) for i in line])

    start = (0, 0)
    end  = (len(maze) - 1, len(maze[len(maze) - 1]) - 1)

    start_node = Node(None, start)
    end_node = Node(Node, end)

    open = []
    closed = []
    found = False

    open.append(start_node)
    while len(open) > 0 and not found:
        current_node = open[0]
        cur_i = 0

        for i, item in enumerate(open):
            if item.total_risk < current_node.total_risk:
                current_node = item
                cur_i = i

        open.pop(cur_i)


        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.risk)
                current = current.parent

            found = True
            break

        print(current_node.__dict__)


        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            new_node = Node(current_node, node_position)
            new_node.risk = maze[node_position[0]][node_position[1]]
            children.append(new_node)

        for child in children:
            new_risk = current_node.risk_to_start + child.risk
            if child in closed or (child in open and new_risk > open[open.index(child)].risk_to_start):
                continue

            child.risk_to_start = new_risk
            child.risk_to_end = abs((child.position[0] - end_node.position[0])) + abs((child.position[1] - end_node.position[1])) + new_risk
            child.total_risk = child.risk_to_start + child.risk_to_end
            closed.append(child)

            for open_node in open:
                if child == open_node and child.risk_to_start > open_node.risk_to_start:
                    continue

            open.append(child)

    print(sum(path))



# part 2
with open("input-day15.txt") as input:
    maze = []
    for line in input:
        line = line.replace("\n", "")
        maze.append([int(i) for i in line])

    width = len(maze[0])
    height = len(maze)

    for i in range(4):
        for row in maze:
            right = [x % 9 + 1 for x in row[-width:]]
            row.extend(right)
        for row in maze[height * i: height*(i+1)]:
            new_row = [x % 9 + 1 for x in row]
            maze.append(new_row)

    start = (0, 0)
    end  = (len(maze) - 1, len(maze[len(maze) - 1]) - 1)

    start_node = Node(None, start)
    end_node = Node(Node, end)

    open = []
    closed = []
    found = False

    open.append(start_node)
    while len(open) > 0 and not found:
        current_node = open[0]
        cur_i = 0

        for i, item in enumerate(open):
            if item.total_risk < current_node.total_risk:
                current_node = item
                cur_i = i

        open.pop(cur_i)


        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.risk)
                current = current.parent

            found = True
            break

        if current_node.risk_to_start % 1000 == 0:
            print(current_node.__dict__)


        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze) - 1]) - 1) or node_position[1] < 0:
                continue

            new_node = Node(current_node, node_position)
            new_node.risk = maze[node_position[0]][node_position[1]]
            children.append(new_node)

        for child in children:
            new_risk = current_node.risk_to_start + child.risk
            if child in closed or (child in open and new_risk > open[open.index(child)].risk_to_start):
                continue

            child.risk_to_start = new_risk
            child.risk_to_end = abs((child.position[0] - end_node.position[0])) + abs((child.position[1] - end_node.position[1])) + new_risk
            child.total_risk = child.risk_to_start + child.risk_to_end
            closed.append(child)

            for open_node in open:
                if child == open_node and child.risk_to_start > open_node.risk_to_start:
                    continue

            open.append(child)

    print(sum(path))
