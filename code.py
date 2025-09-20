class Solution:
    def getLongestPal(self, s):
        # code here

        maxLen =0
        maxLenStr = 0
        maxLenEnd = 0
        def expand(l,r,s):
            nonlocal maxLen, maxLenStr, maxLenEnd
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            curLen = r-l+1-2
            if curLen > maxLen:
                maxLenStr = l+1
                maxLenEnd = r-1
                maxLen = curLen
        for i in range(len(s)):
            # Get the max length of single char middle
            expand(i,i,s)
            expand(i,i+1,s)

        return s[maxLenStr:maxLenEnd+1]
        