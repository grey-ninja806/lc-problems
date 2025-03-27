class solution:
    def two_sum(self, nums, target):
        d={nums[0]:0}
        for i in range(1,len(nums)):
            t=target-nums[i]
            if t in d:
                return [d[t],i]
            d[nums[i]]=i
        return[]
nums=[2,7,11,19]
target=9
k=solution()
print(k.two_sum(nums,target))
