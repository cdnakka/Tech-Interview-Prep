'''
spiral order of elements in the matrix

1) Pop the first row of the matrix
2) Rotate the matrix
3) Back to step 1

'''
from typing import List
def matrix_in_spiral_order(A: List[List[int]])->List[int]:

    matrix = A
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]

    return result

if __name__ =='__main__':
    A = [ [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] ]

    print(matrix_in_spiral_order(A))