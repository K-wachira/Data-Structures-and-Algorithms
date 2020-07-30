# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
    # Keep track of the index9 by maybe a counta every time
    # you go to next and when done compare the counta to pos
    # if pos is not between 0 and counta(final value) return False Else TrueWWWWWWW