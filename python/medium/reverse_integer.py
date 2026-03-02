class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/reverse-integer/
    """

    def reverse(self, x: int) -> int:
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
