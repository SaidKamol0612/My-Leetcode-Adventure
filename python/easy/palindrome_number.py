class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/palindrome-number/)
    """

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return int((str(x))[::-1]) == x


solution = Solution()

# Testcase 1
res = solution.isPalindrome(121)
print(res, end=" ")
print(res)  # Explanation: 121 reads as 121 from left to right and from right to left.

# Testcase 2
res = solution.isPalindrome(
    -121
)  # Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
print(res, end=" ")
print(not res)

# Testcase 3
res = solution.isPalindrome(10)
print(res, end=" ")
print(
    not res
)  # Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
