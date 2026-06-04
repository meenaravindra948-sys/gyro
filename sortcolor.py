def sortColors(nums):
    count = [0] * 3

    for i in nums:
        count[i] += 1

    inx = 0
    for color in range(3):
        for i in range(count[color]):
            nums[inx] = color
            inx += 1

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)