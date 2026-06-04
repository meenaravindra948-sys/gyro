def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]

nums = [1,2,3,4,5]
rotate(nums, 2)
print(nums)