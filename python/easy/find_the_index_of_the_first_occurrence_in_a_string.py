class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/)
    """

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack or len(needle) > len(haystack):
            return -1

        for i in range(len(haystack)):
            if haystack[i : i + len(needle)] == needle:
                return i
        return -1


solution = Solution()

# Testcase 1
res = solution.strStr("sadbutsad", "sad")
print(res, end=" ")
print(res == 0)  # Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.

# Testcase 2
res = solution.strStr("leetcode", "leeto")
print(res, end=" ")
print(res == -1)  # Explanation: "leeto" did not occur in "leetcode", so we return -1.
