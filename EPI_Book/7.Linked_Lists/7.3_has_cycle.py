'''
return if a cycle is present in a linked list
Floyd's cycle detection algo
tortoise and hare problem

'''
def has_cycle(self, head):

    try:
        slow = head
        fast = head.next
        while slow is not fast:
            show = show.next
            fast = fast.next.next
        return True

    except:
        False
