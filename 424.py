class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        maxLen = 0
        start = 0
        maxCount = 0
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1
            maxCount = max(maxCount, count[s[end]])
            if end-start+1-maxCount >k:
                count[s[start]] -= 1
                start += 1
            maxLen = max(maxLen, end-start+1)
        return maxLen
    
    ## slide window，多注意这种解法在这类问题的应用