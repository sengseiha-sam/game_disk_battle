import boad
#test = boad.lst
#print(test)
def setSign(row,col,sign):
    test=boad.lst
    rows = 6
    cols = 7
    
    for i in range(rows):
        for j in range(cols): 
            if i==row and j==col:
                test[i][j] = sign
               
    return test
print(setSign(0,0,'A'))


