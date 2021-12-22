import numpy as np

def get_neighbours_old():

    neighbours_1 = {(0, 0): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (0, 1): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (0, 2): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (1, 0): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (1, 1): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (1, 2): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (2, 0): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (2, 1): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
                    (2, 2): [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]}
    neighbours_2 = {(3, 0): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (3, 1): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (3, 2): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (4, 0): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (4, 1): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (4, 2): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (5, 0): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (5, 1): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)],
                    (5, 2): [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]}
    neighbours_3 = {(6, 0): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (6, 1): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (6, 2): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (7, 0): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (7, 1): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (7, 2): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (8, 0): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (8, 1): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)],
                    (8, 2): [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]}
    neighbours_4 = {(0, 3): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (0, 4): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (0, 5): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (1, 3): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (1, 4): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (1, 5): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (2, 3): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (2, 4): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)],
                    (2, 5): [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]}
    neighbours_5 = {(3, 3): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (3, 4): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (3, 5): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (4, 3): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (4, 4): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (4, 5): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (5, 3): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (5, 4): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)],
                    (5, 5): [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]}
    neighbours_6 = {(6, 3): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (6, 4): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (6, 5): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (7, 3): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (7, 4): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (7, 5): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (8, 3): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (8, 4): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)],
                    (8, 5): [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]}
    neighbours_7 = {(0, 6): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (0, 7): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (0, 8): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (1, 6): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (1, 7): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (1, 8): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (2, 6): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (2, 7): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)],
                    (2, 8): [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]}
    neighbours_8 = {(3, 6): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (3, 7): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (3, 8): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (4, 6): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (4, 7): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (4, 8): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (5, 6): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (5, 7): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)],
                    (5, 8): [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]}
    neighbours_9 = {(6, 6): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (6, 7): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (6, 8): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (7, 6): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (7, 7): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (7, 8): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (8, 6): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (8, 7): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)],
                    (8, 8): [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]}

    neighbours = {**neighbours_1, **neighbours_2, **neighbours_3, **neighbours_4, **neighbours_5, **neighbours_6,
                  **neighbours_7, **neighbours_8, **neighbours_9}

    return neighbours

def get_neighbours():

    neighbours = {}

    tmp = np.zeros((9, 9), dtype = 'int, int')

    for row in range(9):
        for col in range(9):

            tmp[row][col] = (row, col)

    neighbours_1 = [tmp[row][col] for row in range(0, 3) for col in range(0, 3)]
    neighbours_2 = [tmp[row][col] for row in range(3, 6) for col in range(0, 3)]
    neighbours_3 = [tmp[row][col] for row in range(6, 9) for col in range(0, 3)]
    neighbours_4 = [tmp[row][col] for row in range(0, 3) for col in range(3, 6)]
    neighbours_5 = [tmp[row][col] for row in range(3, 6) for col in range(3, 6)]
    neighbours_6 = [tmp[row][col] for row in range(6, 9) for col in range(3, 6)]
    neighbours_7 = [tmp[row][col] for row in range(0, 3) for col in range(6, 9)]
    neighbours_8 = [tmp[row][col] for row in range(3, 6) for col in range(6, 9)]
    neighbours_9 = [tmp[row][col] for row in range(6, 9) for col in range(6, 9)]

    for row in range(0, 3):
        for col in range(0, 3):
            neighbours[(row, col)] = neighbours_1

    for row in range(3, 6):
        for col in range(0, 3):
            neighbours[(row, col)] = neighbours_2

    for row in range(6, 9):
        for col in range(0, 3):
            neighbours[(row, col)] = neighbours_3

    for row in range(0, 3):
        for col in range(3, 6):
            neighbours[(row, col)] = neighbours_4

    for row in range(3, 6):
        for col in range(3, 6):
            neighbours[(row, col)] = neighbours_5

    for row in range(6, 9):
        for col in range(3, 6):
            neighbours[(row, col)] = neighbours_6

    for row in range(0, 3):
        for col in range(6, 9):
            neighbours[(row, col)] = neighbours_7

    for row in range(3, 6):
        for col in range(6, 9):
            neighbours[(row, col)] = neighbours_8

    for row in range(6, 9):
        for col in range(6, 9):
            neighbours[(row, col)] = neighbours_9

    return neighbours

def possible_move(row, col, num):

    global sudoku_state
    global neighbours

    for r in range(len(sudoku_state)):
        if sudoku_state[r][col] == num:
            return False

    for c in range(len(sudoku_state[0])):
        if sudoku_state[row][c] == num:
            return False

    for neighbour in neighbours[(row, col)]:

        if sudoku_state[neighbour[0]][neighbour[1]] == num:

            return False

    return True

def sudoku_solver():

    global sudoku_state
    global neighbours

    # Loop over all positions in the sudoku

    for row in range(len(sudoku_state)):
        for col in range(len(sudoku_state[0])):

            # For each position check if it is 0 which would mean that there is no number there yet

            # If the sudoku is finished, we would loop over all positions and never evaluate the if statement content
            # below in which case we will stop stop the recursion and exit the two for loops above. At this stage we
            # just print the sudoku and it is finished. However, since we have not gone up to the first recursive call
            # yet, the program will still run after the print statement by going to the previous recursive call trying
            # new numbers for each position and so on. Hence it will print all possible solutions if more than one
            # exists.

                if sudoku_state[row][col] == 0:

                    # If the position is empty, we try to put a number num at that position

                    for num in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

                        if possible_move(row, col, num):

                            # If the number num is a legal move then we put num at that position

                            sudoku_state[row][col] = num

                            # Now we have a new state for the sudoku and we call the function that solves sudoku again

                            sudoku_solver()

                            # If we reach this point of the program, it means we looped over all numbers in the list
                            # from 1 to 9 and did not find a possible move. The program skipped the if possible_move
                            # statement and went on to the return statement below. The return statement returns to
                            # where the recursive call came from, which is the line above. The recursive call that
                            # made a call that failed made a legal move that was a wrong move. So we backtrack by
                            # remove the num we put in that position.

                            sudoku_state[row][col] = 0

                            # Now we will try another num for that position by moving to the next num in the for loop.
                            # If we go through the whole num list and do not find a correct move, we will exit the for
                            # loop and call the return which comes after it, which will take us to the previous
                            # recursive call for which we will try the next num in the for loop list and so on.

                    return

    print(np.asarray(sudoku_state))
    sudoku_check(sudoku_state)
    return

def sudoku_check(s):

    for row in s:

        if np.array(row).sum() != 45:

            print('The sudoku has an error.')
            return

    s_transpose = np.array(s).transpose()

    for col in s_transpose:

        if np.array(col).sum() != 45:

            print('The sudoku has an error.')
            return

    print('The sudoku has been solved correctly.')

neighbours = get_neighbours()

sudoku_state = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
                [5, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 8, 7, 0, 0, 0, 0, 3, 1],
                [0, 0, 3, 0, 1, 0, 0, 8, 0],
                [9, 0, 0, 8, 6, 3, 0, 0, 5],
                [0, 5, 0, 0, 9, 0, 6, 0, 0],
                [1, 3, 0, 0, 0, 0, 2, 5, 0],
                [0, 0, 0, 0, 0, 0, 0, 7, 4],
                [0, 0, 5, 2, 0, 6, 3, 0, 0]]

sudoku_solver()
