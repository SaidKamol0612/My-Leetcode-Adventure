class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/power-of-three/)
    """

    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        while n % 3 == 0:
            n = n // 3
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
