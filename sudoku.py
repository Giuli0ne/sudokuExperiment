import time
sudoku0 = [1, 2, 3, 4, 5, 6, 7, 8, 9,
          4, 5, 6, 7, 8, 9, 1, 2, 3,
          7, 8, 9, 1, 2, 3, 4, 5, 6,
          2, 3, 1, 5, 6, 4, 8, 9, 7,
          5, 6, 4, 8, 9, 7, 2, 3, 1,
          8, 9, 7, 2, 3, 1, 5, 6, 4,
          3, 1, 2, 6, 4, 5, 9, 7, 8,
          6, 4, 5, 9, 7, 8, 3, 1, 2,
          9, 7, 8, 3, 1, 2, 6, 4, 5
          ]

sudoku = [0, 4, 0, 0, 0, 0, 1, 7, 9, 
          0, 0, 2, 0, 0, 8, 0, 5, 4, 
          0, 0, 6, 0, 0, 5, 0, 0, 8, 
          0, 8, 0, 0, 7, 0, 9, 1, 0, 
          0, 5, 0, 0, 9, 0, 0, 3, 0, 
          0, 1, 9, 0, 6, 0, 0, 4, 0, 
          3, 0, 0, 4, 0, 0, 7, 0, 0, 
          5, 7, 0, 1, 0, 0, 2, 0, 0, 
          9, 2, 8, 0, 0, 0, 0, 6, 0
          ]

class Sudoku:
    def __init__(self, sudo):
        self.sudo = sudo

    def column(self, columnNumber):
        indices = [i for i in range(81) if (i - columnNumber + 1) % 9 == 0]
        return [self.sudo[i] for i in indices]

    def row(self, rowNumber):
        return self.sudo[9 * (rowNumber-1): 9 * rowNumber]
    
    def square(self, squareNumber):
        first = 27 * ((squareNumber -1)//3) + 3 * ((squareNumber -1)%3)
        r1 = self.sudo[first + 0: (first + 3)]
        r2 = self.sudo[first + 9 : first + 12]
        r3 = self.sudo[first + 18 : first + 21]
        return r1 + r2 + r3
        

    def changeName(self, num1, num2):
        indices1 = [i for i in range(81) if self.sudo[i] == num1]
        indices2 = [i for i in range(81) if self.sudo[i] == num2]
        newsudo = self.sudo
        for i in indices1:
            newsudo[i] = num2
        for i in indices2:
            newsudo[i] = num1
        return Sudoku(newsudo)

    def printSudoku (self):
        for i in range(1, 10):
            print(self.row(i))

    def changeRows(self, rowNum1, rowNum2):
        elements = []
        for i in range(9):
            elements.append(row(self.sudo, i +1))
        temp = elements[rowNum1 -1]
        elements[rowNum1-1] = elements[rowNum2-1]
        elements[rowNum2-1] = temp
        return Sudoku([item for sublist in elements for item in sublist])
    
    def changeColumns(self, rowNum1, rowNum2):
        elements = []
        for i in range(9):
            elements.append(self.column(i +1))
        temp = elements[rowNum1 -1]
        elements[rowNum1-1] = elements[rowNum2-1]
        elements[rowNum2-1] = temp
        s = Sudoku([item for sublist in elements for item in sublist])
        return s.transpose()

    def transpose(self):
        elements = []
        for i in range(9):
            elements.append(self.column(i +1))
        return Sudoku([item for sublist in elements for item in sublist])

    def changeRowBlocks(self, rowBlock1, rowBlock2):
        return (self.changeRows(3 * (rowBlock1 -1 ) + 1, 3 * (rowBlock2 -1) + 1)
        .changeRows(3 * (rowBlock1 -1 ) + 2, 3 * (rowBlock2 -1) + 2)
        .changeRows(3 * (rowBlock1 -1 ) + 3, 3 * (rowBlock2 -1) + 3))

    def changeColumnBlocks(self, columnBlock1, columnBlock2):
        return (self.changeColumns(3 * (columnBlock1 -1 ) + 1, 3 * (columnBlock2 -1) + 1)
        .changeColumns(3 * (columnBlock1 -1 ) + 2, 3 * (columnBlock2 -1) + 2)
        .changeColumns(3 * (columnBlock1 -1 ) + 3, 3 * (columnBlock2 -1) + 3))

    def possible(self, idx, num):
        b1 = num not in self.row((idx // 9) + 1)
        b2 = num not in self.column((idx % 9) + 1)
        b3 = num not in self.square(3 * ((idx // 9) //3) + ((idx % 9) //3) + 1)
        return b1 and b2 and b3
        
    def solve(self):
        for i in range(81):
            if self.sudo[i] == 0:
                for n in range(1,10):
                    if self.possible(i, n):
                        self.sudo[i] = n
                        self.solve()
                        self.sudo[i] = 0
                return Sudoku(self.sudo)
        self.printSudoku()
        input("More?")

#print(row(sudoku,1))
s = Sudoku(sudoku)
# (s.changeColumnBlocks(1,3)
# .changeName(7,2)
# .changeName(9,3)
# .changeName(4,6)
# .changeName(8,9)
# .changeColumnBlocks(2,3)
# .changeColumns(5,6)
# .changeColumns(4,5)
# .printSudoku()
# )

s.solve().printSudoku()
