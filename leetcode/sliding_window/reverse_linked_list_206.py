# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# [1,2,3,4,5]
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head # 1

        while current:
            next_temp = current.next # 3
            current.next = prev # 1
            prev = current # 2
            current = next_temp # 5

        return prev
