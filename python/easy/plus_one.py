class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/power-of-three/)
    """

    def plusOne(self, digits: list[int]) -> list[int]:
        s = ""
        for n in digits:
            s += str(n)
        s = str(int(s) + 1)
        res: list[int] = []
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
