class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/length-of-last-word/)
    """

    def lengthOfLastWord(self, s: str) -> int:
        s.rstrip()
        return len(s.split()[-1])


solution = Solution()

# Testcase 1
res = solution.lengthOfLastWord("Hello World")
print(res, end=" ")
print(res == 5)  # Explanation: The last word is "World" with length 5.

# Testcase 2
res = solution.lengthOfLastWord("   fly me   to   the moon  ")
print(res, end=" ")
print(res == 4)  # Explanation: The last word is "moon" with length 4.

# Testcase 3
res = solution.lengthOfLastWord("luffy is still joyboy")
print(res, end=" ")
print(res == 6)  # Explanation: The last word is "joyboy" with length 6.
