class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/)
    """

    def sumOfThree(self, num: int) -> list[int]:
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
