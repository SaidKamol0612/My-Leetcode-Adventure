class Solution(object):
    """
        # Add Binary

    Difficulty: MEDIUM.

    [View this problem on Leetcode](https://leetcode.com/problems/reverse-integer/)

    ## Description

    Given a signed 32-bit integer `x`, return `x` _with its digits reversed_. If reversin `x` causes the value to go outside the signed 32-bit integer range `[-21**31, 2**31 - 1]`, then return `0`.

    **Assume the environment does not allow you to store 64-bit integers (signed or unsigned).**

    ## Examples

    **Input:** x = 123
    **Output:** 321

    **Input:** x = -123
    **Output:** -321

    **Input:** x = 120
    **Output:** 21

    """

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        symbol = 1

        if x < 0:
            symbol = -1
            x = -x

        res = 0
        while x:
            res = res * 10 + (x % 10)
            x = x // 10

        if 2147483647 < res:
            return 0
        if res < -2147483648:
            return 0
        return res * symbol


solution = Solution()

# Testcase 1
res = solution.reverse(123)
print(res, end=" ")
print(res == 321)

# Testcase 2
res = solution.reverse(-123)
print(res, end=" ")
print(res == -321)

# Testcase 3
res = solution.reverse(120)
print(res, end=" ")
print(res == 21)
