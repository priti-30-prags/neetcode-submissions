class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        l1 = set(())
        for i in nums:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        l = list(d.values()) 
        l.sort(reverse=True)
        for m in range(0,k):
            for i in nums:
                if (d [i] == l[m]):
                    l1.add(i)  
        return list(l1)