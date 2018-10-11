class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = {}
        def judge(s):
            if s == "":
                dp[""] = True
                return True
            for i in range(1,len(s)+1):
                if s[:i] in wordDict:
                    if s[i:] in dp:
                        if dp[s[i:]]:
                            return True
                    else:
                        cc = judge(s[i:])
                        dp[s[i:]] = cc
                        if cc:
                            return True
            return False
        return judge(s)

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False for _ in s]
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word in wordDict and (i==0 or dp[i-1]):
                    dp[j-1] = True
        return dp[len(s)-1]