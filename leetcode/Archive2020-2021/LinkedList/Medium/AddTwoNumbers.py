"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def to_num(self, l1):
        n1 = ''
        while l1 != None:
            n1 = l1.val
            l1 = l1.next
        return int(n1)

    def addTwoNumbers(self, l1, l2) :

        num1 = self.to_num(l1)
        num2 = self.to_num(l2)
        num3 =str(num1[::-1] + num2[::-1])

        l3 = ListNode(int((num3)[-1])) #Init the head as the last number because we are going reverse

        itr = l3

        for numIdx in range(-2, -len(num3) -1, -1):
            itr.next = ListNode(int(num3[numIdx])) #set next val as the second last number
            itr = itr.next  #set the next number as the last val
        return l3

