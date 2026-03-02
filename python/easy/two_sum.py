class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/two-sum/)
    """

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hm = {nums[0]: 0}
        for i in range(1, len(nums)):
            missing = target - nums[i]
            if missing in hm:
                return [i, hm[missing]]
            hm[nums[i]] = i
        return [0, 1]


solution = Solution()

# Testcase 1
res = solution.twoSum([2, 7, 11, 15], 9)
print(
    res, set(res) == {0, 1}
)  # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Testcase 2
res = solution.twoSum([3, 2, 4], 6)
print(res, set(res) == {1, 2})

# Testcase 3
res = solution.twoSum([3, 3], 6)
print(res, set(res) == {0, 1})
