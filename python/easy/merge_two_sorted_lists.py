from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next


class Solution(object):
    """
        # Merge Two Sorted Lists

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)

    ## Description

    You are given the heads of two sorted linked lists `list1` and `list2`.

    Merge the two lists into **sorted** list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the _merged linked list_.

    ## Examples

    **Input:** list1 = [1, 2, 4], list2 = [1, 3, 4]
    **Output:** [1, 1, 2, 3, 4, 4]

    **Input:** list1 = [], list2 = []
    **Output:** []

    **Input:** list1 = [], list2 = [0]
    **Output:** [0]
    """

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 or not list2:
            return list1 or list2

        curr = ListNode(-101, None)
        first = ListNode(-101, curr)

        while curr != None and list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = ListNode(list1.val, list2)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val, list1)
                list2 = list2.next

            curr = curr.next

        return first.next.next


solution = Solution()


def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


# Testcase 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
res = solution.mergeTwoLists(list1, list2)
print_list(res)
print(
    res == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
)

# Testcase 2
list1 = None
list2 = None
res = solution.mergeTwoLists(list1, list2)
print_list(res)
print(res == None)

# Testcase 3
list1 = None
list2 = ListNode(0)
res = solution.mergeTwoLists(list1, list2)
print_list(res)
print(res == ListNode(0))
