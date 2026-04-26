class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        max_count = 0
        for i in n: 
            if i-1 not in n:
                count = 1
                j  = i
                while j+1 in n:
                    j= j+1
                    count = count+1
                max_count = max(max_count,count)
        return max_count