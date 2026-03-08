from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result: list[list[int]] = []

        for row_idx in range(numRows):
            pre = result[row_idx - 1] if row_idx > 0 else []
            row: list[int] = [1]

            for col_idx in range(1, row_idx + 1):
                if col_idx == row_idx:
                    row.append(1)
                else:
                    row.append(pre[col_idx - 1] + pre[col_idx])

            result.append(row)

        return result


solution = Solution()


# Testcase 1
res = solution.generate(5)
print(res, end=" ")
print(
    res
    == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
    ]
)

# Testcase 2
res = solution.generate(1)
print(res, end=" ")
print(
    res
    == [
        [1],
    ]
)
