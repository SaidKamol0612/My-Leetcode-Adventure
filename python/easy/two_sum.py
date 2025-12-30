class Solution(object):
    """
        # Two Sum
    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/two-sum/)

    ## Description
    Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

    You may assume that each input would have **exactly one solution**, and you amy not use the same element twice.

    You can return the answer in any order.

    ## Examples

    **Input:** nums = [2, 7, 11, 15], target = 9
    **Output:** [0, 1]

    **Input:** nums = [3, 2, 4], target = 6
    **Output:** [1, 2]

    **Input:** nums [3, 3], target = 6
    **Output:** [0, 1]
    """

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hm = {nums[0]: 0}
        for i in range(1, len(nums)):
            missing = target - nums[i]
            if missing in hm:
                return [i, hm[missing]]
            hm[nums[i]] = i


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
