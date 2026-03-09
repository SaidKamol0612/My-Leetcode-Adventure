from typing import Optional, Self


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[Self] = None,
        right: Optional[Self] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        val = str(self.val)
        if self.left:
            val += " -> " + self.left.__repr__()

        if self.right:
            val += " -> " + self.right.__repr__()

        return val


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


solution = Solution()

# Testcae 1
p = TreeNode(1, TreeNode(2), TreeNode(3))
q = TreeNode(1, TreeNode(2), TreeNode(3))
res = solution.isSameTree(p, q)
print(res, end=" ")
print(res)

# Testcae 2
p = TreeNode(1, TreeNode(2))
q = TreeNode(1, None, TreeNode(2))
res = solution.isSameTree(p, q)
print(res, end=" ")
print(not res)

# Testcae 2
p = TreeNode(1, TreeNode(2), TreeNode(1))
q = TreeNode(1, TreeNode(1), TreeNode(2))
res = solution.isSameTree(p, q)
print(res, end=" ")
print(not res)
