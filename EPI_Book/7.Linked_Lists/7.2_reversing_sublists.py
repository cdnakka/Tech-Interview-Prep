'''
Given a singly linked list and a start point and end point defining a sublist within the list; return the list with the sublist reversed
'''

from typing import List, Optional

class ListNode():
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def reverse_sublist(L: ListNode, start = int, finish = int) -> Optional(ListNode):
    dummy_head = sublist_head = ListNode(0, L)

    #get the starting point of sublist to be reversed, keep the remaining list as is
    for _ in range (1, start):
        sublist_head = sublist_head.next

    #reverse_sublist
    #iterator
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        sublist_iter, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return dummy_head.next

