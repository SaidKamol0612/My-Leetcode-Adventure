class Solution(object):
    """
        # Search Insert Position

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/search-insert-position/)

    ## Description

    Given a sorted array of distinct integers and a target value, return the index if the target is found. If, not, return the index where it would be if it were inserted in order.

    You must write an algorithm with `0(log n)` runtime complexity.

    ## Examples

    **Input:** nums = [1, 3, 5, 6], target = 5
    **Output:** 2

    **Input:** nums = [1, 3, 5, 6], target = 2
    **Output:** 1

    **Input:** nums = [1, 3, 5, 6], target = 7
    **Output:** 4
    """

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not target in nums:
            nums.append(target)
            nums.sort()
            return nums.index(target)
        else:
            return nums.index(target)


solution = Solution()

# Testcase 1
res = solution.searchInsert([1, 3, 5, 6], 5)
print(res, end=" ")
print(res == 2)

# Testcase 2
res = solution.searchInsert([1, 3, 5, 6], 2)
print(res, end=" ")
print(res == 1)

# Testcase 3
res = solution.searchInsert([1, 3, 5, 6], 7)
print(res, end=" ")
print(res == 4)
