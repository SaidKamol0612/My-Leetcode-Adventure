class Solution(object):
    """
        # Find Subarrays With Equal Sum

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/find-subarrays-with-equal-sum/)

    ## Description

    Given a **0-indexed** integer array `nums`, determine whether there exist **two** subarrays of length `2` with **equal** sum. Note that the two subarrays must begin at **different** indices.

    Return `true` _if these subarrays exist, and `false` otherwise_.

    A **subarray** is a contigous non-empty sequence of elements within an array.

    ## Examples

    **Input:** nums = [4, 2, 4]
    **Output:** True

    **Input:** nums = [1, 2, 3, 4, 5]
    **Output:** False

    **Input:** nums = [0, 0, 0]
    **Output:** True
    """

    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
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
    res == True
)  # Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.

# Testcase 2
res = solution.findSubarrays([1, 2, 3, 4, 5])
print(res, end=" ")
print(res == False)  # Explanation: No two subarrays of size 2 have the same sum.

# Testcase 3
res = solution.findSubarrays([0, 0, 0])
print(res, end=" ")
print(
    res == True
)  # Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
# Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.
