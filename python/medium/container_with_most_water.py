class Solution(object):
    """
    [View this problem on Leetcode](https://leetcode.com/problems/container-with-most-water/)
    """

    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        left = 0
        right = len(height) - 1
        while left < right:
            border = min(height[left], height[right])
            area = border * (right - left)
            max_area = max(area, max_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


solution = Solution()

# Testcase 1
res = solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(res, end=" ")
print(res == 49)

# Testcase 2
res = solution.maxArea([1, 1])
print(res, end=" ")
print(res == 1)
