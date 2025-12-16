class Solution(object):
    """
        # Longest Palindromic Substring

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/power-of-three/)

    ## Description

    Given an integer `n`, return `true` _if it is a power of three. Otherwise, return `false`_.

    An integer `n` is a power of three, if there exists an integer `x` such that `n == 3**x`.

    Examples:

    **Input:** digits = [1,2,3]
    **Output:** [1,2,4]

    **Input:** digits = [4,3,2,1]
    **Output:** [4,3,2,2]

    **Input:** digits = [9]
    **Output:** [1,0]
    """

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        for n in digits:
            s += str(n)
        s = str(int(s) + 1)
        res = []
        for c in s:
            res.append(int(c))

        return res


solution = Solution()

# Testcase 1
res = solution.plusOne([1, 2, 3])
print(res, end=" ")
print(res == [1, 2, 4])

# Testcase 2
res = solution.plusOne([4, 3, 2, 1])
print(res, end=" ")
print(res == [4, 3, 2, 2])  # Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Testcase 1
res = solution.plusOne([9])
print(res, end=" ")
print(res == [1, 0])  # Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
