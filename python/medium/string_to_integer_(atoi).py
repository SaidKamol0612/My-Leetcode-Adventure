class Solution(object):
    """
        # Add Binary

    Difficulty: MEDIUM.

    [View this problem on Leetcode](https://leetcode.com/problems/string-to-integer-atoi/)

    ## Description

    Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer.

    The algorithm for `myAtoi(string s)` is as follow:

    1. **Whitespace:** Ignore any leading(`" "`).
    2. **Signedness:** Determine the sign by checking if the next character is `'-'` or `'+'`, assuming positivity if neither present.
    3. **Conversion:** Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
    4. **Rounding:** If the integer is out 32-bit signed integer range `[-2**31, 2**31 - 1]`, then round the integer to remain in the range. Specifically, integers less than `-2**31` should be rounded to `-2**31`, and integers greater than `2**31 - 1` should be rounded to `2**31 - 1`.

    Return the integer as the final result.

    ## Examples

    **Input:** s = "42"
    **Output:** 42

    **Input:** s = " -042"
    **Output:** -42

    **Input:** s = "1337c0d3"
    **Output:** 1337

    **Input:** s = "0-1"
    **Output:** 0

    **Input:** s = "words and 987"
    **Output:** 0
    """

    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1 or s.isspace():
            return 0

        s = s.lstrip()

        symbol = 1
        if s[0] == "-":
            symbol = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        res = "0"
        for c in s:
            if c.isdigit() and c not in "+-.":
                res += c
            else:
                break

        res = int(res) * symbol
        if -2147483648 >= res:
            return -2147483648
        elif res >= 2147483648:
            return 2147483647

        return res


solution = Solution()

# Testcase 1
res = solution.myAtoi("42")
print(res, end=" ")
print(res == 42)
# Explanation:

# The underlined characters are what is read in and the caret is the current reader position.
# Step 1: "42" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "42" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "42" ("42" is read in)

# Testcase 2
res = solution.myAtoi("   -042")
print(res, end=" ")
print(res == -42)
# Explanation:

# Step 1: "   -042" (leading whitespace is read and ignored)
#             ^
# Step 2: "   -042" ('-' is read, so the result should be negative)
#              ^
# Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)


# Testcase 3
res = solution.myAtoi("1337c0d3")
print(res, end=" ")
print(res == 1337)
# Explanation:

# Step 1: "1337c0d3" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)
#              ^


# Testcase 4
res = solution.myAtoi("0-1")
print(res, end=" ")
print(res == 0)
# Explanation:

# Step 1: "0-1" (no characters read because there is no leading whitespace)
#          ^
# Step 2: "0-1" (no characters read because there is neither a '-' nor '+')
#          ^
# Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)

# Testcase 4
res = solution.myAtoi("words and 987")
print(res, end=" ")
print(res == 0)
# Explanation:

# Reading stops at the first non-digit character 'w'.
