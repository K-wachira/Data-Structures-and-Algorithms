# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def to_int(self, l1):
        num=  ''
        while l1 != None:

            num = num +str(l1.val)
            l1= l1.next
        return (num)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.to_int(l1)
        num2 = self.to_int(l2)
        numlist = []

        for i in num1:
            numlist.append(int(i))
        for i in num2:
            numlist.append(int(i))
        numlist.sort()

        l3 = ListNode(numlist[0])

        itr = l3
        for i in range(len(numlist)):
            itr.next = ListNode(i)
            itr = itr.next
        return l3


