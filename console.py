import boad
def printboard():
    
    num = ""
    for i in range(len(boad.array_of_board)):
        
        for j in range(len(boad.array_of_board[i])):
            num = num + str(boad.array_of_board[i][j]) + " "  
        num += "\n" 
    print(num)          
printboard()


