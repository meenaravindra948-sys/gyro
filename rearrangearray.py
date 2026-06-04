def rearrangeArray(nums):
        # pos = []
        # neg = []
        # for i in nums:
        #     if i>=0:
        #         pos.append(i)
        #     else:
        #         neg.append(i)
        # ans = []    
        # for i in range(len(pos)):
        #     ans.append(pos[i])
        #     ans.append(neg[i])

        # return ans

        ans=[0]* len(nums)

        pos =0
        neg =1

        for num in nums:
            if num >0:
                ans[pos] = num
                pos+=2
            else:
                ans[neg] = num
                neg+=2
        return ans        

nums=[3,1,-2,-5,2,-4]
print(rearrangeArray(nums))