'''
consider 2 sorted lists L1 and L2, return the list containing the merged lists in ascending order

Brute force: O((n+m)log(n+m))
merging 2 lists and then sorting them again

'''
from typing import List, Optional
class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def merge_two_sorted_lists(L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:

    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next, L1 = L1, L1.next
        
        else:
            tail.next, L2 = L2, L2.next

        tail = tail.next

    #remaining elements of L1 and L2
    tail.next = L1 or L2
    return dummy_head.next