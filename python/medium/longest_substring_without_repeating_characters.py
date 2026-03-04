class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0

        hp: dict[str, int] = {}
        left = 0
        right = 0
        while right < len(s):
            if s[right] in hp:
                left = max(left, hp[s[right]] + 1)

            hp[s[right]] = right
            longest = max(right - left + 1, longest)
            right += 1

        return longest


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
