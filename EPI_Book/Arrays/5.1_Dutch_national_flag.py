'''
Arrange like colors together;
Arrange numbers less than pivot together at the front and numbers greater than pivot at the last
'''
from typing import List

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    #first pass, group elements smaller than pivot
    smaller = 0
    larger = len(A) - 1

    for i in range(len(A)):
        if A[i] < pivot:
            A[smaller], A[i] = A[i], A[smaller]
            smaller += 1

    #second pass move larger elements to the ending
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[larger], A[i] = A[i], A[larger]
            larger -= 1

    return A

# if there are elements of equal value to the pivot

def dutch_flag_partition_2(pivot_index: int, A: List[int]) -> None:

    pivot = A[pivot_index]
    smaller, equal , larger = 0, 0, len(A)-1

    # predefine resulting sub-array sequences accordingly:
    # smaller: A[:smaller]
    # equal: A[smaller:equal]
    # larger: A[equal:larger]

    while equal < larger:

        if A[equal] < pivot:
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller, equal = smaller + 1, equal +1 

        elif A[equal] == pivot:
            equal +=1
        
        else: #A[equal] > pivot:
            
            
            A[equal], A[larger] = A[larger], A[equal]
            larger -= 1
            
            
    return A

if __name__ =='__main__':

    pivot = 3
    A = [4,2,5,2,1,4,6,8]
    A = dutch_flag_partition(pivot, A)  #variation 1
    print(A)
