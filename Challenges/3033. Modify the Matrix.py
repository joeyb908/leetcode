# Given a 0-indexed m x n integer matrix matrix, create a new 0-indexed matrix called answer. Make answer equal to matrix, then replace each element with the value -1 with the maximum element in its respective column.

# In more simple terms, for every element -1, replace it with the maximum element in the same column.

def modifiedMatrix(matrix):# columns
    answer = matrix.copy()
    curColMax = [0] * len(matrix)
    replaceIndex = [(0,0,0)] * len(matrix)
    row = 0

    for r in matrix:
        
        for c in range(0, len(matrix[0])):
            curColMax[c] = max(curColMax[c], r[c])

            if r[c] == -1 and replaceIndex[row][2] < curColMax[c]:
                replaceIndex[row] = [row, c, curColMax[c]]
            # if matrix[r][c] == -1:
            #     replaceIndex = c
            # if c == len(matrix[0])-1 and replaceIndex != -1:
            #     answer[r[c]]= curColMax
        row += 1


    

    return answer

print(modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))