class Solution:
    """
    [View this problem on Leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
    """

    def removeDuplicates(self, nums: list[int]) -> int:
        nums[:] = sorted(list(set(nums)))
        return len(nums)


solution = Solution()


# Custom judge
def test_remove_duplicates(n: list[int], e: list[int]):
    nums = n  # Input array
    expected_nums = e  # The expected answer with correct length

    k = solution.removeDuplicates(nums)  # Calls the your implementation

    assert k == len(expected_nums)
    for i in range(k):
        assert nums[i] == expected_nums[i]
    return True


# Testcase 1
nums = [1, 1, 2]
expected_nums = [1, 2]
res = test_remove_duplicates(nums, expected_nums)
print(
    res
)  # Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Testcase 2
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expected_nums = [0, 1, 2, 3, 4]
res = test_remove_duplicates(nums, expected_nums)
print(
    res
)  # Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
