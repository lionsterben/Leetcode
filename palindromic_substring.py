class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = {}
        res = 0
        for ll in range(1,len(s)+1):
            for ind in range(0, len(s)-ll+1):
                st = s[ind:ind+ll]
                # print(st)
                if len(st) == 1:
                    dp[(ind, ind+ll)] = True
                    res += 1
                else:
                    if s[ind] != s[ind+ll-1]:
                        dp[(ind, ind+ll)] = False
                        continue
                    if not s[ind+1: ind+ll-1] or dp[(ind+1,ind+ll-1)]:
                        dp[(ind, ind+ll)] = True
                        res += 1
                    else:
                        dp[(ind, ind+ll)] = False
        return res

class Solution:
    def countSubstrings(self, S):
        N = len(S)
        res = 0
        for ind in range(2*N-1):
            left = ind // 2
            right = left + ind % 2
            while left >= 0 and right <= N-1 and S[left] == S[right]:
                res += 1
                left -= 1
                right += 1
        return res
剪枝没剪好