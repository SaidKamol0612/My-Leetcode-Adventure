class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/merge-sorted-array/)
    """

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
        if m < 1:
            nums1[:] = nums2
        nums1[:] = nums1[:m]
        res = nums1
        res.extend(nums2)
        res.sort()
        nums1[:] = res


solution = Solution()

# Testcase 1
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
res = solution.merge(nums1, 3, nums2, 3)
print(nums1, end=" ")
print(
    nums1 == [1, 2, 2, 3, 5, 6]
)  # Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Testcase 2
nums1 = [1]
nums2 = []
res = solution.merge(nums1, 1, nums2, 0)
print(nums1, end=" ")
print(nums1 == [1])  # Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Testcase 3
nums1 = [0]
nums2 = [1]
res = solution.merge(nums1, 0, nums2, 1)
print(nums1, end=" ")
print(nums1 == [1])  # Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
