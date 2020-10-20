sampleBoard = [
    [0, 3, 0, 1, 5, 0, 0, 2, 6],
    [1, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 2, 0, 0, 9, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 4, 0],
    [7, 2, 0, 0, 0, 0, 0, 1, 5],
    [4, 0, 9, 0, 0, 0, 3, 0, 0],
    [0, 4, 1, 6, 3, 7, 0, 0, 5],
    [0, 0, 0, 9, 0, 0, 2, 0, 0],
    [3, 9, 0, 0, 0, 8, 4, 0, 0],
]

def printBoard(board):
    """ 
    Prints the state of the board in a formatted way 
    """
    bar = ["—" for _ in range(len(board)*4//3 + 1)]
    printedRows = 0
    for row in sampleBoard:
        if printedRows % 3 == 0:
            print(*bar, sep=" ")
        outputRow = row[:]
        addedBars = 0
        for i in range(len(row) + 1):
            if i%3 == 0:
                outputRow.insert(i + addedBars, "|")
                addedBars += 1
        print(*outputRow, sep= " ")
        printedRows += 1
    print(*bar, sep=" ")

printBoard(sampleBoard)
