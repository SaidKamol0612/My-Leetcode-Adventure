class Solution(object):
    """
        # Valid Parentheses

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/valid-parentheses/)

    ## Description

    Given an string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

    An input string is valid if:

    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

    ## Examples

    **Input:** s = "()"
    **Output:** true

    **Input:** s = "()[]{}"
    **Output:** true

    **Input:** s = "(]"
    **Output:** false

    **Input:** s = "([])"
    **Output:** true

    **Input:** s = "([)]"
    **Output:** false
    """

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) < 2 or len(s) % 2 != 0:
            return False

        t = []
        for c in s:
            if c in "([{":
                t.append(c)
            else:
                if not t:
                    return False

                top = t.pop()
                if c == ")" and top != "(":
                    return False
                elif c == "]" and top != "[":
                    return False
                elif c == "}" and top != "{":
                    return False
        return not t


solution = Solution()

# Testcase 1
res = solution.isValid("()")
print(res, end=" ")
print(res == True)

# Testcase 2
res = solution.isValid("()[]{}")
print(res, end=" ")
print(res == True)

# Testcase 3
res = solution.isValid("(]")
print(res, end=" ")
print(res == False)

# Testcase 4
res = solution.isValid("([])")
print(res, end=" ")
print(res == True)

# Testcase 5
res = solution.isValid("([)]")
print(res, end=" ")
print(res == False)
