
array_of_board =[]
rows = 6
cols = 7
for i in range(rows):
    array_of_board.append([])
    for j in range(cols):
        array_of_board[i].append(0)  

        
def setSign(row,col,sign):
    newarray = array_of_board
    
    rows = 6
    cols = 7
    
    for i in range(rows):
        for j in range(cols): 
            if i==row and j==col:
                
                newarray[i][j] = sign
            

    return newarray
print(setSign(0,0,'A'))




