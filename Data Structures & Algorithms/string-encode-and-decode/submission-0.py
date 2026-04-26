class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        print(strs)
        for i in strs:
            s = s + str(len(i)) + "#" + i 
        return s
    def decode(self, s: str) -> List[str]:
        l = []
        i = 0
        while i < len(s):
            strs = ""
            n = ""
            while s[i] != "#":
                n= n+s[i]
                i = i+1
            i = i+1
            strs = s[i:i+int(n)]
            l.append(strs)
            i=i+int(n)
        return l
