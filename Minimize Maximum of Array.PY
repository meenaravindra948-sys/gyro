class Solution:
    def minimizeArrayValue(self, nums):
        ans = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            ans = max(ans, (prefix_sum + i) // (i + 1))

        return ans

nums = [3, 7, 1, 6]

obj = Solution()
result = obj.minimizeArrayValue(nums)

print(result)