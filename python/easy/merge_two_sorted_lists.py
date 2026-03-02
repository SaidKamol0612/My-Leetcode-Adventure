from typing import Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val and self.next == other.next

    def __repr__(self) -> str:
        val = str(self.val)
        if self.next:
            return val + " -> " + self.next.__repr__()
        else:
            return val


class Solution(object):
    """
    [View this problem on Leetcode](https://leetcode.com/problems/merge-two-sorted-lists/)
    """

    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        if not list1 or not list2:
            return list1 or list2

        dump_head = ListNode(-101, ListNode(-101, None))
        curr = dump_head

        while curr and list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 or list2
        return dump_head.next


solution = Solution()


# Testcase 1
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
res = solution.mergeTwoLists(list1, list2)
print(res, end=" ")
print(
    res == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
)

# Testcase 2
list1 = None
list2 = None
res = solution.mergeTwoLists(list1, list2)
print(res, end=" ")
print(res is None)

# Testcase 3
list1 = None
list2 = ListNode(0)
res = solution.mergeTwoLists(list1, list2)
print(res, end=" ")
print(res == ListNode(0))
