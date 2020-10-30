import tkinter as tk
import tkinter.font as font
import solver as s

size = range(9)

class SolverGUI:
    def __init__(self, root):
        buttonFont = font.Font(family='Courier', size=20)

        inputFrame = tk.Frame(root, width= 300, height = 300)
        inputFrame.pack(padx=20, pady= 20, side = 'left')
        outputFrame = tk.Frame(root, width= 342, height = 300)
        outputFrame.pack(padx=20, pady= 20, side= 'right')

        inGrid = self.makeGrid(inputFrame, size)

        clearButton = tk.Button(inputFrame, text='Clear', font= buttonFont, command=lambda: self.clearGrid(inGrid))
        solveButton = tk.Button(inputFrame, text="Solve", font= buttonFont, command=lambda: self.displayGrid(outputFrame, inGrid))
        quitButton = tk.Button(inputFrame, text='Quit', font= buttonFont, command=root.quit)

        clearButton.grid(columnspan = 3, row= 10, column = 0, pady = 20, ipadx = 10)
        solveButton.grid(columnspan = 3, row= 10, column = 3, pady = 20, ipadx = 10)
        quitButton.grid(columnspan = 3, row= 10, column = 6, pady = 20, ipadx = 10)

        

    def solveGrid(self, entryGrid):
        """
        Returns:
            A 2d int array representation of the solved sodoku board
        """
        grid = []
        for entryRow in entryGrid:
            row = []
            for entry in entryRow:
                val = entry.get()
                if val == "":
                    val = 0
                row.append(int(val))
            grid.append(row)
        return s.solve(grid)
    
    def displayGrid(self, master, entryGrid):
        """
        Effect:
            Display the inputed 2D int array in master
        """
        intGrid = self.solveGrid(entryGrid)
        for y in size:
            for x in size:
                square = tk.Label(master, text= str(intGrid[y][x]), width = 2, font= ('Courier', 25), justify= 'center')
                square.grid(row=y, column = x)
    
    def clearGrid(self, entryGrid):
        """
        Effect:
            Clear the entries in the input grid
        """
        [[entry.delete(0, 'end') for entry in entryRow] for entryRow in entryGrid]

    def makeGrid(self, master, size):
        """
        Effect: 
            Constructs 
        
        Returns:
            blah
        """
        grid = []
        for y in size:
            row = []
            for x in size:
                square = tk.Entry(master, width = 2, font= ('Robot Mono', 25), justify= 'center')
                square.grid(row=y, column = x)
                row.append(square)
            grid.append(row)
        return grid

root = tk.Tk(className="sudoku solver")
gui = SolverGUI(root)
root.resizable(False, False)
root.mainloop()