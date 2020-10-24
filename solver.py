sampleBoard = [
    [0, 3, 0, 1, 5, 0, 0, 2, 6],
    [1, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 2, 0, 0, 9, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 4, 0],
    [7, 2, 0, 0, 0, 0, 0, 1, 5],
    [4, 0, 9, 0, 0, 0, 3, 0, 0],
    [0, 4, 1, 6, 3, 7, 0, 0, 0],
    [0, 0, 0, 9, 0, 0, 2, 0, 0],
    [3, 9, 0, 0, 0, 8, 4, 0, 0],
]

fullBoard = [
    [1, 3, 1, 1, 5, 1, 1, 2, 6],
    [1, 1, 1, 1, 1, 1, 1, 8, 1],
    [1, 1, 2, 1, 1, 9, 1, 1, 1],
    [1, 8, 1, 1, 1, 1, 1, 4, 1],
    [7, 2, 1, 1, 1, 1, 1, 1, 5],
    [4, 1, 9, 1, 1, 1, 3, 1, 1],
    [1, 4, 1, 6, 3, 7, 1, 1, 5],
    [1, 1, 1, 9, 1, 1, 2, 1, 1],
    [3, 9, 1, 1, 1, 8, 4, 1, 1],
]

def printBoard(board):
    """ 
    Prints the state of the board in a formatted way 
    """
    bar = ["—" for _ in range(len(board)*4//3 + 1)]
    printedRows = 0
    for row in board:
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

def getCol(x, board):
    """
    Returns:    
        A list containing a copy of the integers in column x
    Requires:   
        0 <= x <= 8
    """
    if (x > 8 or x < 0):
        return []
    else:
        return [row[x] for row in board]

def getRow(y, board):
    """
    Returns:    
        A list containing a copy of the integers in row y
    Requires:   
        0 <= y <= 8
    """
    if (y > 8 or y < 0):
        return []
    else:
        return board[y][:]

def setElem(x, y, board, int):
    """
    Effect:     
        Set's element at (x, y) on board to int
    Returns:    
        True if element was successfully placed
        False if an element already existed
    """
    if (board[y][x] == 0):
        board[y][x] = int
        return True
    return False

def cloneBoard(board):
    """
    Returns a deep copy of the inputted board.
    """
    copy = []
    copy.extend([[elem for elem in row] for row in board])
    return copy

def getFullestIncomplete(getFunc, board):
    """
    Params:    
        getFunc (func): Either getRow or getCol
    Returns:    
        The index of the row/column with the least positive number of 0's, 
        and the number of 0's as a tuple. 
        If all rows/columns are filled (i.e no 0's), return -1 as the index. 
        If more than one row/column share the least positive number of 0's 
        the row/column with the lower index is returned.
    """
    minIndex = -1
    minZeroCount = 10
    for i in range(len(board)):
        zeroCount = getFunc(i, board).count(0)
        if (zeroCount != 0 and zeroCount < minZeroCount):
            minZeroCount = zeroCount
            minIndex = i
    return (minIndex, minZeroCount)

def missing(list):
    """
    Returns a list containing the integers from 1...9 missing in list
    """
    missingInts = []
    for i in range(9):
        if (i+1) not in list:
            missingInts.append(i+1)
    return missingInts

def fillInOne(board, lstOfInts, newInt, rowOrColIndex, isRow):
    """
    Params:
        lstOfInts (list): The list containing the integers of a row or column on the board to be mutated
        newInt (int) : The integer that will replace the 0
        rowOrColIndex (int): Index of the row or col inputed to lstOfInts
        isRow (bool): True if the inputted lst is a row, False if the inputted lst is a col
        
    Effect:     
        Mutates the specifed rowOrCol on the board by replacing one of the 0's with a valid integer. 
        If there are more than one 0's the lowest index is replaced.
        If no 0's exist nothing happens.
    """
    if isRow:
        for x in range(len(lstOfInts)):
            if (lstOfInts[x] == 0):
                setElem(x, rowOrColIndex, board, newInt)
                return
    else:
        for y in range(len(lstOfInts)):
            if (lstOfInts[y] == 0):
                setElem(rowOrColIndex, y, board, newInt)
                return

def containsDuplicate(list):
    """
    Returns true if the list contains duplicate integers other than 0
    """
    noZeroList = [num for num in list if num > 0]
    tempSet = set(noZeroList)
    return len(noZeroList) != len(tempSet)

def isValid(board):
    """
    Checks if the board contains any duplicate numbers along the rows and columns
    """
    if (any([containsDuplicate(getRow(i,board)) for i in range(len(board))]) or 
       any([containsDuplicate(getCol(j,board)) for j in range(len(board))])):
        return False
    return True

def solve(board):
    """
    Returns:    
        A completed version of the board, derived from mutating a copy of the board inputted 
        board is not mutated.
    """
    # Find the most filled out row / columns
        # if getFullestIncompleteReturns for both getRow and getCol returns -1, then done
        # if  ^ returns (i, 1), then fill in that one spot (certain) and call solve directly
    # Clone the board and set one of the places to a possible value
    # Call solve on the board. 
    if not isValid(board):
        return
    (rowIndex, rowZeroNum) = getFullestIncomplete(getRow, board)
    (colIndex, colZeroNum) = getFullestIncomplete(getCol, board)
    if rowIndex == -1 and colIndex == -1:
        return board
    elif rowZeroNum <= colZeroNum:
        row = getRow(rowIndex, board)
        for missingInt in missing(row):
            newBoard = cloneBoard(board)
            fillInOne(newBoard, row, missingInt, rowIndex, True)
            # printBoard(newBoard)            #debugging
            solvedBoard = solve(newBoard)
            if solvedBoard:
                return solvedBoard
    else:
        col = getCol(colIndex, board)
        for missingInt in missing(col):
            newBoard = cloneBoard(board)
            fillInOne(newBoard, col, missingInt, colIndex, False)
            # printBoard(newBoard)            #debugging
            solvedBoard = solve(newBoard)
            if solvedBoard:
                return solvedBoard