class Solution(object):
    """
        # Find Three Consecutive Integers That Sum to a Given Number

    Difficulty: MEDIUM.

    [View this problem on Leetcode](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/)

    ## Description

    Given an integer `num`, return _three consecutive integers (as a sorted array) that **sum** to `num`_. If `num` cannot be expressed as the sum of three consecutive integers, return an **empty** array.

    ## Examples

    **Input:** num = 33
    **Output:** [10, 11, 12]

    **Input:** num = 4
    **Output:** []
    """

    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num % 3 != 0:
            return []

        num = num // 3
        return [num - 1, num, num + 1]


solution = Solution()

# Testcase 1
res = solution.sumOfThree(33)
print(res, end=" ")
print(res == [10, 11, 12])  # Explanation: 33 can be expressed as 10 + 11 + 12 = 33.
# 10, 11, 12 are 3 consecutive integers, so we return [10, 11, 12].

# Testcase 2
res = solution.sumOfThree(4)
print(res, end=" ")
print(
    res == []
)  # Explanation: There is no way to express 4 as the sum of 3 consecutive integers.
