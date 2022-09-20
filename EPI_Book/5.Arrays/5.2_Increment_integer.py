'''
Increment a integer represented in the form onf an array with 1
for ex: 

    [1,2,4,5] + 1 = [1,2,4,6]
    [0,1,9] + 1 = [0,2,0]
'''
from typing import List

def increment_integer(A: List[int]) -> List[int]:

    A[-1] += 1

    for i in reversed(range(len(A))):

        # if A[i] // 10:
        #     A[i] = A[i] % 10
        #     A[i-1] += 1
        # incrementing only by 1, noyt by 9

        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0]//10:
        A[0] = 1
        A.append(0)

    return A

if __name__ =='__main__':

    A = [4,2,5,2,1,4,6,9]
    A = increment_integer(A)  #variation 1
    print(A)
