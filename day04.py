# part 1
with open("input-day04.txt") as input:
    numbers = []
    boards = []
    board_i = -1

    for line in input:
        if numbers == []:
            numbers = [int(n) for n in line.split(",")]
        elif line != "\n":
            boards[board_i].append([int(n) for n in line.split(" ") if n != ""])
        else:
            board_i += 1
            boards.append([])

    for num in numbers:
        for board in boards:
            for x in range(0, len(board)):
                for y in range(0, len(board[x])):
                    if board[x][y] == num:
                        board[x][y] = None

            for x in range(0, len(board)):
                if all([n == None for n in board[x]]):
                    break
                
            for y in range(0, len(board[0])):
                if all([board[x][y] == None for x in range(0, len(board))]):
                    break
            else:
                continue
            break
        else:
            continue
        break


    total = sum([n for row in board for n in row if n != None])

    print(total * num)

# part 2
with open("input-day04.txt") as input:
    numbers = []
    boards = []
    board_i = -1

    for line in input:
        if numbers == []:
            numbers = [int(n) for n in line.split(",")]
        elif line != "\n":
            boards[board_i].append([int(n) for n in line.split(" ") if n != ""])
        else:
            board_i += 1
            boards.append([])

    for num in numbers:
        for b in range(0, len(boards)):
            board = boards[b]
           
            for x in range(0, len(board)):
                for y in range(0, len(board[x])):
                    if board[x][y] == num:
                        board[x][y] = None

            for x in range(0, len(board)):
                if board != [[]] and all([n == None for n in board[x]]):
                    boards_in_play = len([1 for b in boards if b != [[]]])
                    if boards_in_play == 1:
                        break
                    else:
                        boards[b] = [[]]
                        
                
            for y in range(0, len(board[0])):
                if board != [[]] and all([board[x][y] == None for x in range(0, len(board))]):
                    boards_in_play = len([1 for b in boards if b != [[]]])
                    if boards_in_play == 1:
                        break
                    else:
                        boards[b] = [[]]          
            else:
                continue
            break
        else:
            continue
        break

    total = sum([n for row in board for n in row if n != None])
    print(total * num)
