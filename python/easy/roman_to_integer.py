class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/roman-to-integer/)
    """

    def romanToInt(self, s: str) -> int:
        nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = nums[s[0]]
        for i in range(1, len(s)):
            pre = s[i - 1]
            c = s[i]
            if pre == "I" and c in ("V", "X"):
                res -= 1
                res += nums[c] - 1
            elif pre == "X" and c in ("L", "C"):
                res -= 10
                res += nums[c] - 10
            elif pre == "C" and c in ("D", "M"):
                res -= 100
                res += nums[c] - 100
            else:
                res += nums[c]
        return res


solution = Solution()

# Testcase 1
res = solution.romanToInt("III")
print(res, end=" ")
print(res == 3)  # Explanation: III = 3.

# Testcase 2
res = solution.romanToInt("LVIII")
print(res, end=" ")
print(res == 58)  # Explanation: L = 50, V= 5, III = 3.

# Testcase 3
res = solution.romanToInt("MCMXCIV")
print(res, end=" ")
print(res == 1994)  # Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
