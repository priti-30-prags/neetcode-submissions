class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0,len(nums)):
            t = target - nums[i]           
            if t in d: 
                return [d[t],i]
            d[nums[i]] = i 
        return None