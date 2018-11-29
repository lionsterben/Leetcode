class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict, length = set(wordDict), len(s)
        res = []
        # dp = {}
        def get_sentence(i, cur):
            if i == length:
                res.append(cur)
                return
            for idx in range(i+1, length+1):
                if s[i:idx] in wordDict:
                    if i == 0:
                        new_cur = cur + s[i:idx]
                    else:
                        new_cur = cur + (' '+s[i:idx])
                    # cur += (' '+s[i:idx])
                    get_sentence(idx, new_cur)
        get_sentence(0, "")
        return res

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = {} ## store index
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                word = s[i:j]
                if word in wordDict and (i-1 in dp or i == 0):
                    if i == 0:
                        dp[j-1] = [0]
                    else:
                        if j-1 in dp:
                            dp[j-1].append(i)
                        else:
                            dp[j-1] = [i]
        res = []
        def dfs(end, path):
            # print(end)
            if end == -1:
                res.append(path[1:])
                return
            for idx in dp.get(end,[]):
                word = s[idx:end+1]
                dfs(idx-1, " "+word+path)
        # print(dp)
        dfs(len(s)-1,"")
        return res