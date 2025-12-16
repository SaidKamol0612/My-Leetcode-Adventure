class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subs = []

        m = 1
        for start in range(len(s)):
            for end in range(start + m, len(s)):
                if s[start] in s[start + 1:end]:
                    break
                
                sub = s[start:end]
                print(sub)
                set_sub = set(list(sub))
                if len(sub) == len(set_sub):
                    if m < len(sub):
                        m = len(sub)
                    subs.append(len(sub))
        return max(subs)


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
