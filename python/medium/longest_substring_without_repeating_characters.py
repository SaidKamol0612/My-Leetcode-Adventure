class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        longest_sub = 1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in s[i:j]:
                    longest_sub = max(j - i, longest_sub)
                    break
            else:
                longest_sub = max(len(s) - i, longest_sub)

        return longest_sub


solution = Solution()

# Testcase 1
res = solution.lengthOfLongestSubstring("abcabcbb")
print(res, end=" ")
print(res == 3)  # Explanation: The answer is "abc", with the lentg of 3.

# Testcase 2
res = solution.lengthOfLongestSubstring("bbbb")
print(res, end=" ")
print(res == 1)  # Explanation: The answer is "b", with the lentg of 1.

# Testcase 3
res = solution.lengthOfLongestSubstring("pwwkew")
print(res, end=" ")
print(res == 3)  # Explanation: The answer is "wke", with the lentg of 3.
# Notice that thr answer must be a substring, "pwke" is a subsequencse and not a substring.
