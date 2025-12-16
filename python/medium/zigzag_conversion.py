import math

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        num_cols = math.ceil(len(s) / numRows)

        # Preallocate m with None (or spaces) so you can assign later
        m = [[None for _ in range(num_cols)] for _ in range(numRows)]

        col = 0
        n = 0
        i = 0

        while i < len(s):
            if n == numRows:
                n = 0
                col += 1
            m[n][col] = s[i]

            i += 1
            n += 1
        print(m)


solution = Solution()

# Testcase 1
res = solution.convert("PAYPALISHIRING", 3)
print(res, end=" ")
print(res == "PAHNAPLSIIGYIR")
