"""
This is a simple problem that merely tests your ability to manipulate list node pointers.
Because the input list is sorted, we can determine if a node is a duplicate by comparing its

value to the node after it in the list. If it is a duplicate, we change the next pointer of the current
node so that it skips the next node and points directly to the one after the next node.
"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        current = head.next  #set the current to be on step og the head
        prev = head #set the head to be one step behind the current

        while current: #when current  is not none ( empty)

            if current.val == prev.val: # if two numbers following each other eg 1 and 1
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head


" 1->1->2 "