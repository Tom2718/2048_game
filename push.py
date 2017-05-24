#push
#T Tumiel
#21 Apr

def push_up (grid):
    """merge grid values upwards"""
    #push up
    for i in range(3):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row-1][column] == 0 and row > 0:
                    grid[row-1][column] = grid[row][column]
                    grid[row][column] = 0 
    #merge values up
    for row in range(len(grid)-1):
        for column in range(len(grid[row])):
            if grid[row][column] > 0:
                if grid[row][column] == grid[row+1][column]:
                    grid[row][column] *= 2
                    grid[row+1][column] = 0    
    #push up once more for the new holes created
    for i in range(2):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if row > 0:
                    if grid[row-1][column] == 0:
                        grid[row-1][column] = grid[row][column]
                        grid[row][column] = 0    
    return grid



def push_down (grid):
    """merge grid values downwards"""
    #push down
    for i in range(3):
        for row in range(len(grid)-2,-1,-1):
            for column in range(len(grid[row])):
                if grid[row+1][column] == 0:
                    grid[row+1][column] = grid[row][column]
                    grid[row][column] = 0
            
    #merge
    for row in range(len(grid)-1, 0,-1):
        for column in range(len(grid[row])):
            if grid[row][column] > 0:
                if grid[row][column] == grid[row-1][column]:
                    grid[row][column] *= 2
                    grid[row-1][column] = 0
                            
    #push down once more for the new holes created
    for i in range(2):
        for row in range(len(grid)-2,-1,-1):
            for column in range(len(grid[row])):
                if grid[row+1][column] == 0:
                    grid[row+1][column] = grid[row][column]
                    grid[row][column] = 0    
                    
    return grid
 
 
 
def push_left (grid):
    """merge grid values left"""
    #push left
    for i in range(3):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if column > 0:
                    if grid[row][column-1] == 0:
                        grid[row][column-1] = grid[row][column]
                        grid[row][column] = 0
    
    #merge
    for row in range(len(grid)):
        for column in range(len(grid[row])-1):
            if grid[row][column] > 0:
                if grid[row][column] == grid[row][column+1]:
                    grid[row][column] *= 2
                    grid[row][column+1] = 0
                          
    #push left once more for the new holes created
    for i in range(2):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if column > 0:
                    if grid[row][column-1] == 0:
                        grid[row][column-1] = grid[row][column]
                        grid[row][column] = 0    

    return grid
 
 
 
def push_right (grid):
    """merge grid values right"""     
    #push right
    for i in range(3):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if column < 3:
                    if grid[row][column+1] == 0:
                        grid[row][column+1] = grid[row][column]
                        grid[row][column] = 0
            
    #merge
    for row in range(len(grid)):
        for column in range(len(grid[row])-2,-1,-1):
            if grid[row][column] > 0:
                if grid[row][column] == grid[row][column+1]:
                    grid[row][column+1] *= 2
                    grid[row][column] = 0
                               
    #push right once more for the new holes created
    for i in range(2):
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if column < 3:
                    if grid[row][column+1] == 0:
                        grid[row][column+1] = grid[row][column]
                        grid[row][column] = 0    

    return grid


