import math
grid = [
    [7,0,0,0,3,4,8,0,0],
    [8,0,4,6,0,0,0,0,0],
    [0,3,9,0,5,0,0,0,0],
    [1,0,0,5,0,0,6,0,0],
    [0,4,0,7,0,9,0,3,0],
    [0,0,3,0,0,8,0,0,9],
    [0,0,0,0,7,0,3,2,0],
    [0,2,6,0,0,1,9,0,5],
    [0,0,7,9,0,0,0,0,4]
]

areaSize = int(math.sqrt(len(grid)))
print(areaSize)

def findTarget(target, area):
    row = area//areaSize
    if (area % 3 != 0):
        row+=1
    col = area - (area//areaSize)*areaSize
    if col ==0:
        col = 3  
    for r in range((row*3)-3,row*3):
        for c in range((row*3)-3,col*3):
            if (grid[r][c] == target):
                return True        
    return False

print(str(findTarget(0,6)))