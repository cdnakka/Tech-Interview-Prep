'''
remove one char in a string and replace a char in a string with another string using a single forward and backwartd pass
doing a insert and replace will ential shifting the array to the left and right and resulting in O(n^2) complexity

'''
from typing import List
def replace_remove(size: int, s: List[str]):

    #forward iteration, remove all 'b' s and count all a's :
    write_idx, a_count = 0,0
    for i in range(size):
        if s[i] != 'b':
            s[write_idx] =s[i]
            write_idx +=1
        if s[i] == 'a':
            a_count +=1

    #backward pass for removing 'a' s and adding up d's
    cur_idx = write_idx - 1   # index used for backward pass
    write_idx += a_count -1     # index used to prserve number of a's which are counted double
    final_len = write_idx + 1

    while cur_idx >= 0:
        if s[cur_idx] == 'a':
            s[write_idx - 1: write_idx + 1] = 'dd'
            write_idx -=2
        
        else: 
            s[write_idx] = s[cur_idx]
            write_idx -=1
        cur_idx -=1

    return final_len , s

if __name__ == '__main__':

    a = ['a','c','d','b','b','c','a']
    size = 7
    print(replace_remove(size, a))
