class Solution:
    """
        # Roman To Integer
    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/roman-to-integer/)

    ## Description
    Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

    | **Symbol** | **Value** |
    |:----------:|:---------:|
    |   I        |   1       |
    |   V        |   5       |
    |   X        |   10      |
    |   L        |   50      |
    |   C        |   100     |
    |   D        |   500     |
    |   M        |   1000    |

    For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X` + `II`. The number `27` is written as `XXVII`, which is `XX` + `V` + `II`.

    Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:
    * `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
    * `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
    * `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

    Given a roman numeral, convert it to an integer.

    ## Examples

    **Input:** s = "III"
    **Output:** 3

    **Input:** s = "IV"
    **Output:** 4

    **Input:** s = "MCMXCIV"
    **Output:** 1994
    """

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
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
