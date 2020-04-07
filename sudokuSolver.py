import math, time

x1 = [5,0,0,0,1,0,0,0,4]
x2 = [2,7,4,0,0,0,6,0,0]
x3 = [0,8,0,9,0,4,0,0,0]

x4 = [8,1,0,4,6,0,3,0,2]
x5 = [0,0,2,0,3,0,1,0,0]
x6 = [7,0,6,0,9,1,0,5,8]

x7 = [0,0,0,5,0,3,0,1,0]
x8 = [0,0,5,0,0,0,9,2,7]
x9 = [1,0,0,0,2,0,0,0,3]

table = [x1,x2,x3,
         x4,x5,x6,
         x7,x8,x9]

startTime = time.time()


# Loop to fill up colums list.
def get_columns():
    col = []
    for n in range(9):
        column = []
        for m in range(9):
            column.append(table[m][n])
        col.append(column)
    return col


# Making boxes list.
def get_boxes():
    """x should stay the same for 3 rounds and y should always change from 0 to 2"""
    box = []

    yC = 0 # Counter for y
    poss = [(0, 3), (3, 6), (6, 9)]
    
    for c in range(9):
        selectBox = []
        y = poss[yC]
        if c < 3:
            x = poss[0]
        elif c > 5:
            x = poss[2]
        else:
            x = poss[1]

        for i in range(3):
            selectBox += table[x[0] : x[1]][i][y[0] : y[1]]


        # End of a loop, check if y is 2
        if yC == 2:
            yC = 0
        else:
            yC += 1
        
        box.append(selectBox)

    return box


# Inputs codinates and returns box, get_box(0,6) == box[6]
def get_box(x,y, box):
    x = math.ceil((x+1)/3)-1
    y = math.ceil((((y+1)/3))-1)*3
    return box[x+y]


# Function that takes row index as an input and changes the table
def check_row(tableNum):
    # Finding numbers missing in the first row
    notIn = []
    columns = get_columns()
    box = get_boxes()
    
    for i in range(10):
        if i in table[tableNum]:
            pass
        else:
            notIn.append(i)
    
    # Checking first row for zeros and then checking cloumns and box.
    for i in range(len(table[tableNum])):
        possible = 0
        number = 0
        
        if table[tableNum][i] == 0:
            for num in notIn:
                if num not in columns[i] and num not in get_box(i,tableNum,box):
                    number = num
                    possible += 1
                    if possible > 1:
                        break
                
            if possible == 1: # Solution!
                table[tableNum][i] = number # Put number in table 
                notIn.remove(number) # Remove number from notIn list
                
                columns = get_columns() # Update cloumns
                box = get_boxes() # update Boxes 


# Loop thoght the rows
def trySolve():
    for num in range(9):
        check_row(num)


# Fucntion that counts unsolved spaces
def countZero():
    count = 0
    for l in table:
        for num in l:
            if num == 0:
                count += 1
    return count


# Finally a solving fucntion
def solve():
    print('Solving...')
    while True:
        count = countZero()
        trySolve()
        if count == 0:
            printTable()
            print('\nSolved in: %s seconds.' %round((time.time() - startTime), 5))
            break

# Print table
def printTable():
    for l in table:
        print(l)


printTable()
solve()
