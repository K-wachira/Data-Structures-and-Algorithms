# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = sort_list= ListNode(0)
        node1 = l1; node2 = l2
        while (node1 or node2):
            if None == node1:
                sort_list.next = node2
                break
            elif None == node2:
                sort_list.next = node1
            elif node1.val > node2.val:
                sort_list.next = sort_list = ListNode(node2.val)
                node2 = node2.next
            else:
                sort_list.next = sort_list= ListNode(node1.val)
                node1 = node1.next
        return head.next


