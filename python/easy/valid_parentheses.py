class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/valid-parentheses/)
    """

    def isValid(self, s: str) -> bool:
        # if len(s) < 2 or len(s) % 2 != 0:
        #     return False

        parentheses = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        opened: list[str] = []
        for c in s:
            if c in parentheses:
                opened.append(c)
            else:
                if len(opened) == 0 or parentheses[opened[-1]] != c:
                    return False
                opened.pop()

        return len(opened) == 0


solution = Solution()

# Testcase 1
res = solution.isValid("()")
print(res, end=" ")
print(res)

# Testcase 2
res = solution.isValid("()[]{}")
print(res, end=" ")
print(res)

# Testcase 3
res = solution.isValid("(]")
print(res, end=" ")
print(not res)

# Testcase 4
res = solution.isValid("([])")
print(res, end=" ")
print(res)

# Testcase 5
res = solution.isValid("([)]")
print(res, end=" ")
print(not res)
