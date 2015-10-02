#!/usr/local/bin/python3.4


__author__ = 'ee364e10'

"""
Lab03 for ECE 364:
"""

def checkIfMAtrixIsValid(matrix):
    a = len(matrix)
    for i in range(a-1):
        b = len(matrix[i])
        if (b != len(matrix[i+1])):
            return False
    return True

def getMatrixSize(matrix):
    valid = checkIfMAtrixIsValid(matrix)
    c=[0,0]
    if (valid == True ):
        c[0] = len(matrix)
        c[1] = len(matrix[0])
    else:
        c=[]
    return c

def getRow(matrix,rowIndex):
    valid = checkIfMAtrixIsValid(matrix)
    if (valid == False):
        uu = []
        return uu
    size = getMatrixSize(matrix)
    if (size[0] < rowIndex):
        c = []
        return c
    else:
        y = matrix[rowIndex]
        return y

def getColumn(matrix,columnIndex):
    valid = checkIfMAtrixIsValid(matrix)
    if (valid == False):
        yy = []
        return yy
    size = getMatrixSize(matrix)
    if (size[1] < columnIndex):
        c = []
        return c
    else:
        y =[]
        for i in range(size[0]):
            y.append(matrix[i][columnIndex])
        return y

def transposeMatrix(matrix):
    valid = checkIfMAtrixIsValid(matrix)
    if (valid == False):
        yy = []
        return yy
    size = getMatrixSize(matrix)
    col = size[1]
    row = size[0]
    trans = []
    for i in range(col):
        trans.append([])
        for j in range(row):
            trans[i].append(matrix[j][i])
    return trans

def dotProduct(row,col):
    if ( len(row) == len(col)):
        #print("Checkpoint 10")
        if (len(row) != 0):
            #print("Checkpoint 20")
            if (len(col)!=0):
                #print("Checkpoint 30")
                d = 0
                for i in range(len(row)):
                    d = d + (row[i]*col[i])
            return d


def multiplyMatrices(matrix1, matrix2):

    ch1 = checkIfMAtrixIsValid(matrix1)
    ch2 = checkIfMAtrixIsValid(matrix2)
    if (ch1 is False) & (ch2 is False):
        return
    #print("Checkpoint 1")
    s1 = getMatrixSize(matrix1)
    s2 = getMatrixSize(matrix2)

    row = s1[0]
    col = s2[1]

    cR = (s1[1] == s2[0])

    #print("Checkpoint 3: {} -> {}".format(row,col))
    if (cR is False):
        return
    #print("Checkpoint 2")
    result = [[0]* col for i in range(row) ]

    for r in range(row):
        for c in range(col):
            #print("Checkpoint 4: {} -> {}".format(matrix1[r],matrix2[c]))
            #print("Checkpoint 5: {} -> {}".format(r,c))
            result[r][c] = dotProduct(getRow(matrix1,r),getColumn(matrix2,c))
            #print("Checkpoint 6: {}".format(result[r][c]))
    return result



if __name__ == "__main__":
    mat1= [[3,2,8]]
    mat2=[[0,-1,-1],[4,-3,8],[-3,-3,2]]
    c = multiplyMatrices(mat1,mat2)
    print("{}".format(c))