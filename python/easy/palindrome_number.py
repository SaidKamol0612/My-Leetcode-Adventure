class Solution(object):
    """
        # Palindrome Number

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/palindrome-number/)

    ## Description

    Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

    <details>
    <summary>Palindrome is</summary>
    An integer is a palindrome when it reads the same forward and backward.

    For example, `121` is a palindrome while `123` is not.

    </details>

    ## Examples

    **Input:** x = 121
    **Output:** true

    **Input:** x = -121
    **Output:** false

    **Input:** x = 10
    **Output:** false
    """

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        return int((str(x))[::-1]) == x


solution = Solution()

# Testcase 1
res = solution.isPalindrome(121)
print(res, end=" ")
print(
    res == True
)  # Explanation: 121 reads as 121 from left to right and from right to left.

# Testcase 2
res = solution.isPalindrome(
    -121
)  # Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
print(res, end=" ")
print(res == False)

# Testcase 3
res = solution.isPalindrome(10)
print(res, end=" ")
print(
    res == False
)  # Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
