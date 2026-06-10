class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pt1 = 0
        p = nums
        p.sort()
        r = []
        while pt1<len(nums)-2:
            pt2 = pt1+1
            pt3 = len(nums)-1
            while pt2<pt3:
                l = []
                if (p[pt1]+p[pt2]+p[pt3])==0:
                    l = [p[pt1],p[pt2],p[pt3]]
                    l.sort()
                    if l not in r:
                        r.append(l)
                    pt2 += 1
                    pt3 -= 1
                elif p[pt1]+p[pt2]+p[pt3] > 0:
                    pt3 -= 1
                else:
                    pt2 += 1
            pt1 += 1
        return r