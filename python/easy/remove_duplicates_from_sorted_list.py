# Definition for singly-linked list.
from typing import Self


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


class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
    """

    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head


solution = Solution()

# Testcase 1
head = ListNode(1, ListNode(1, ListNode(2)))
res = solution.deleteDuplicates(head)
print(res, end=" ")
print(res == ListNode(1, ListNode(2)))

# Testcase 2
head = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
res = solution.deleteDuplicates(head)
print(res, end=" ")
print(res == ListNode(1, ListNode(2, ListNode(3))))
