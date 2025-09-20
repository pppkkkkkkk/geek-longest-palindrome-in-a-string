class Solution:
    def getLongestPal(self, s):
        # # code here

        # maxLen =0
        # maxLenStr = 0
        # maxLenEnd = 0
        # def expand(l,r,s):
        #     nonlocal maxLen, maxLenStr, maxLenEnd
        #     while l>=0 and r<len(s) and s[l] == s[r]:
        #         l-=1
        #         r+=1
        #     curLen = r-l+1-2
        #     if curLen > maxLen:
        #         maxLenStr = l+1
        #         maxLenEnd = r-1
        #         maxLen = curLen
        # for i in range(len(s)):
        #     # Get the max length of single char middle
        #     expand(i,i,s)
        #     expand(i,i+1,s)

        # return s[maxLenStr:maxLenEnd+1]
        
        
        if not s:
            return ""
        
        start = 0
        max_length = 1
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            # Odd length palindromes (e.g., "aba")
            l1, r1 = expand(i, i)
            len1 = r1 - l1 + 1
            if len1 > max_length:
                max_length = len1
                start = l1
            
            # Even length palindromes (e.g., "abba")
            l2, r2 = expand(i, i + 1)
            len2 = r2 - l2 + 1
            if len2 > max_length:
                max_length = len2
                start = l2
                
        return s[start : start + max_length]