from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

obj = Solution()
obj.rotate(nums, k)

print(nums)