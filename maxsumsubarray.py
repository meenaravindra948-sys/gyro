def maxSubArray(nums):
        curr_sum= nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            curr_sum=curr_sum + nums[i]
            max_sum = max(curr_sum,max_sum)

            if curr_sum<0:
                curr_sum = 0

        return max_sum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))