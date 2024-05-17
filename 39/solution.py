import json

def es39(n, jsonFile):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    x, y = 0, 0                                             
    directions =[0,1], [1,0], [0, -1], [-1, 0]               
    dir = 0                                                 
    for i in range(1, n*n+1):                               
        matrix[y][x] = i                                   
        ny = y + directions[dir][0]                          
        nx = x + directions[dir][1]                          
        if not (0 <= nx < n and 0 <= ny < n and matrix[ny][nx] == 0):  
            dir = (dir + 1) % 4                             
            ny = y + directions[dir][0]                      
            nx = x + directions[dir][1]                      
        x,y = nx,ny                                         
    counter = 0                                               
    for x in range(0, n, 2):                                
        for y in range(n):
            counter += matrix[y][x]
    with open(jsonFile, mode='w', encoding='utf8') as f:    
        json.dump(matrix, f)
    return counter
