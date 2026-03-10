from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        from math import factorial as f
        
        result = [1]
        for col_idx in range(1, rowIndex + 1):
            if col_idx == rowIndex:
                result.append(1)
            else:
                result.append(
                    f(rowIndex) // (f(col_idx) * f(rowIndex - col_idx))
                )
        return result


solution = Solution()


# Testcase 1
res = solution.getRow(3)
print(res, end=" ")
print(res == [1, 3, 3, 1])

# Testcase 2
res = solution.getRow(0)
print(res, end=" ")
print(res == [1])

# Testcase 3
res = solution.getRow(1)
print(res, end=" ")
print(res == [1, 1])
