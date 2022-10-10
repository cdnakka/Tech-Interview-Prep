'''
remove duplicates from sorted array
'''

from typing import List
def removeDuplicates(nums: List[int]) -> int:

    if not nums:
        return 0

    #l = len(nums)
    pointer = 0
    for i in range(1,len(nums)):
        if nums[pointer] != nums[i]:
            nums[pointer+1] = nums[i]
            pointer += 1

    return nums

if __name__ =='__main__':
    A = [ 1, 4, 4, 4, 5, 6, 7, 8, 9 ]

    print(removeDuplicates(A))