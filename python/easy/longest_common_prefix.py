class Solution(object):
    """
        # Longest Common Prefix

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/longest-common-prefix/)

    ## Description

    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string `""`.

    ## Examples

    **Input:** strs = ["flower", "flow", "flight"]
    **Output:** "fl"

    **Input:** strs = ["dog", "racecar", "car"]
    **Output:** ""
    """

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = list(set(strs))

        prefix = ""
        i = 0
        while i < len(strs[0]):
            prefix += strs[0][i]
            for s in strs:
                if not s.startswith(prefix):
                    return prefix[: len(prefix) - 1 :] if len(prefix) > 0 else ""
            i += 1
        return prefix


solution = Solution()

# Testcase 1
res = solution.longestCommonPrefix(["flower", "flow", "flight"])
print(res, end=" ")
print(res == "fl")

# Testcase 2
res = solution.longestCommonPrefix(["dog", "racecar", "car"])
print(res, end=" ")
print(res == "")  # Explanation: There is no common prefix among the input strings.
