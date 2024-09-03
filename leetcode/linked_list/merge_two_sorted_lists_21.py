# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # list1 = [1,3,4], list2 = [1, 2, 4]
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Создание первого связанного списка: list1 = [1,2,4]
list1 = create_linked_list([1, 2, 4])

# Создание второго связанного списка: list2 = [1,3,4]
list2 = create_linked_list([1, 3, 4])

sol = Solution()
print(sol.mergeTwoLists(list1, list2))