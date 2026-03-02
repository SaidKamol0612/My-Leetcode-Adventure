class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/sqrtx/)
    """

    def mySqrt(self, x: int) -> int:
        import math

        # i = 0
        # while i * i <= x:
        #     i += 1
        # return i - 1

        return int(math.sqrt(x))


solution = Solution()

# Testcase 1
res = solution.mySqrt(4)
print(res, end=" ")
print(res == 2)  # Explanation: The square root of 4 is 2, so we return 2.

# Testcase 1
res = solution.mySqrt(8)
print(res, end=" ")
print(
    res == 2
)  # Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
