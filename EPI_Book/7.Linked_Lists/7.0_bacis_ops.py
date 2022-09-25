'''
Basic Operations : search, insert , delete
'''
from typing import List, Optional, Union

class ListNode:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

def search_list(L:ListNode, key: int) -> ListNode:
    while L & L.data != key:
        L = L.next
    return L

def insert_after(node:ListNode, new_node: ListNode) -> None:
    new_node.next = node.next
    node.next = new_node

def delete_node(node:ListNode) -> None:
    node.next = node.next.next
