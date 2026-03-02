class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/string-to-integer-atoi/)
    """

    def myAtoi(self, s: str) -> int:
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
