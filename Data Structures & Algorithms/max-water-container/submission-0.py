class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max1 = 0
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                ar = min(heights[i],heights[j]) * (j-i)
                if ar > max1:
                    max1 = ar
        return max1