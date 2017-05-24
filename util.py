#util
#T Tumiel
#21 Apr

import copy

def create_grid(grid):
    """create a 4x4 array of zeroes within grid"""
    for i in range(4):
        grid.append([0,0,0,0])


def print_grid (grid):
    """print out a 4x4 grid in 5-width columns within a box"""
    print('+'+ '-'*20 + '+')
    for i in range(len(grid)):
        print('|',end='')
        for j in range(len(grid[i])):
            if grid[i][j] != 0:
                print('{0:<5}'.format(grid[i][j]),end='')
            else:
                print(' '*5,end='')
        print('|')
    print('+'+ '-'*20 + '+')
            
            
grid = [[1,2,3,4],[5,6,7,0],[9,10,11,12],[13,14,15,16]]

def check_lost (grid):
    """return True if there are no 0 values and there are no
    adjacent values that are equal; otherwise False"""
    for i in grid:
        if i.count(0) > 0:
            return False
    else:
        for i in range((len(grid))):
            for j in range((len(grid[i])-1)):
                if grid[i][j] == grid[i][j+1]:
                    return False
        else:
            for i in range((len(grid))-1):
                    for j in range((len(grid[i]))):            
                        if i <3:
                            if grid[i][j] == grid[i+1][j]:
                                return False
    return True


def check_won (grid):
    """return True if a value>=32 is found in the grid; otherwise
    False"""
    for i in grid:
        for j in i:
            if j>=32:
                return True
    return False


def copy_grid (grid):
    """return a copy of the given grid"""
    newGrid = copy.deepcopy(grid)
    return newGrid


def grid_equal (grid1, grid2):
    """check if 2 grids are equal - return boolean value"""    
    if grid1 == grid2:
        return True
    return False