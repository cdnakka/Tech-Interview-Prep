'''
Select a subset of the array which gives a subset of size k from teh array length of n. 
All subsets should be equally likely
Return output in the main array itself
'''
import random
from typing import List
def sample_offline_data(k : int, A: List[int]) -> List[int]:

    for i in range(k):
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]

    return A

if __name__ =='__main__':

    A = [4,5,2,6,2,7,9,2,8,1]
    print(f'input array : {A}')
    random_sample = sample_offline_data(5,A)
    print(random_sample)