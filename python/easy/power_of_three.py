class Solution(object):
    """
        # Longest Palindromic Substring

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/power-of-three/)

    ## Description

    Given an integer `n`, return `true` _if it is a power of three. Otherwise, return `false`_.

    An integer `n` is a power of three, if there exists an integer `x` such that `n == 3**x`.

    ## Examples

    **Input:** n = 27
    **Output:** true

    **Input:** n = 0
    **Output:** false

    **Input:** n = -1
    **Output:** false
    """

    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n / 3
        return n == 1


solution = Solution()

# Testcase 1
res = solution.isPowerOfThree(27)
print(res, end=" ")
print(res == True)  # Explanation: 27 = 3**3

# Testcase 2
res = solution.isPowerOfThree(0)
print(res, end=" ")
print(res == False)  # Explanation: There is no x where 3**x = 0.

# Testcase 3
res = solution.isPowerOfThree(-1)  # Explanation: There is no x where 3**x = (-1).
print(res, end=" ")
print(res == False)
