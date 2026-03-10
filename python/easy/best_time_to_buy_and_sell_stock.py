from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = prices[0], prices[-1]
        profit = 0
        for p in prices:
            if p < buy:
                buy = sell = p

            if p > sell:
                sell = p

            profit = max(profit, sell - buy)

        return profit


solution = Solution()


# Testcase 1
res = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(res, end=" ")
print(res == 5)

# Testcase 2
res = solution.maxProfit([7, 6, 4, 3, 1])
print(res, end=" ")
print(res == 0)
