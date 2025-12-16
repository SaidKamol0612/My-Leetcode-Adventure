class Solution(object):
    """
        # Remove Element

    Difficulty: EASY.

    [View this problem on Leetcode](https://leetcode.com/problems/remove-element/)

    ## Description

    Given an integer array `num` and an integer `val` in `nums` [in-place](https://en.wikipedia.org/wiki/In-place_algorithm). The order of the elements may be changed. Then return _the number of elements in_ `nums` _which are not equal to_ `val`.

    Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

    - Change the array `nums` such that first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
    - Return `k`.

    ## Examples

    **Input:** nums = [3, 2, 2, 3], val = 3
    **Output:** 2, nums = [2, 2, _, _]

    **Input:** nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
    **Output:** 5, nums = [0, 1, 4, 0, 3, _, _, _]
    """

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        res = []
        for i in range(len(nums)):
            if nums[i] != val:
                res.append(nums[i])
        nums[:] = res
        return len(nums)


solution = Solution()


# Custom judge
def test_removeElement(n, v, e):
    nums = n  # Input array
    val = v  # Value to remove
    expected_nums = e  # The expected answer with correct length

    k = solution.removeElement(nums, val)  # Calls the your implementation

    assert k == len(expected_nums)
    sorted(nums)  # Sort the first k elements of nums
    for i in range(k):
        assert nums[i] == expected_nums[i]
    return True


# Testcase 1
nums = [3, 2, 2, 3]
val = 3
expected_nums = [2, 2]
res = test_removeElement(nums, val, expected_nums)
print(
    res
)  # Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Testcase 2
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
expected_nums = [0, 1, 3, 0, 4]
res = test_removeElement(nums, val, expected_nums)
print(
    res
)  # Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
