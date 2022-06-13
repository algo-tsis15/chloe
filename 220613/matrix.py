import math

def solution(matrix_sizes):
    table = [[math.inf for i in range(len(matrix_sizes))] for j in range(len(matrix_sizes))]
    
    for i in range(len(matrix_sizes)):
        table[i][i] = 0
    
    for i in range(1, len(matrix_sizes)):
        for j in range(len(matrix_sizes)):
            k = i + j
            
            if k >= len(matrix_sizes):
                break
            for l in range(j,k):
                table[j][k] = min(
                    table[j][k], table[j][l] + table[l+1][k] + (matrix_sizes[j][0] * matrix_sizes[l][1] * matrix_sizes[k][1])
                )
                
    return table[0][-1]