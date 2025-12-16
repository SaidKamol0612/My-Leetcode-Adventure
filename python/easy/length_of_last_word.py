class Solution(object):
    """
        # Length of Last Word

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/length-of-last-word/)

    ## Description

    Given a string `s` consisting of words and spaces, return _the length of the_ **last** _word in the string_.

    A **word** is a maximal substring consisting of non-space characters only.

    <details>

    <summary>Substring is</summary>

    a contiguous non-empty sequence of characters within a string.

    </details>

    ## Examples

    **Input:** s = "Hello World"
    **Output:** 5

    **Input:** s = "   fly me   to   the moon  "
    **Output:** 4

    **Input:** s = "luffy is still joyboy"
    **Output:** 6
    """

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
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
