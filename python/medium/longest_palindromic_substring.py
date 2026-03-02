class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/longest-palindromic-substring/)
    """

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = s[0]
        m = 1
        for start in range(len(s)):
            for end in range(start + m, len(s) + 1):
                c = s[start:end]
                if c == c[::-1]:
                    if m < (end - start):
                        m = end - start
                        res = c
        return res


solution = Solution()

# Testcase 1
res = solution.longestPalindrome("babad")
print(res, end=" ")
print(res == "bab")  # Explanation: "aba" is also a valid answer.

# Testcase 2
res = solution.longestPalindrome("cbbd")
print(res, end=" ")
print(res == "bb")
