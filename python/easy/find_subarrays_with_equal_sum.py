class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/find-subarrays-with-equal-sum/)
    """

    def findSubarrays(self, nums: list[int]) -> bool:
        # s = []
        # for i in range(len(nums) - 1):
        #     k = nums[i] + nums[i + 1]
        #     if k in s:
        #         return True
        #     s.append(k)
        # return False

        k = [nums[i] + nums[i + 1] for i in range(len(nums) - 1)]
        return len(k) != len(set(k))


solution = Solution()

# Testcase 1
res = solution.findSubarrays([4, 2, 4])
print(res, end=" ")
print(
    res
)  # Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.

# Testcase 2
res = solution.findSubarrays([1, 2, 3, 4, 5])
print(res, end=" ")
print(not res)  # Explanation: No two subarrays of size 2 have the same sum.

# Testcase 3
res = solution.findSubarrays([0, 0, 0])
print(res, end=" ")
print(
    res
)  # Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
# Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.
