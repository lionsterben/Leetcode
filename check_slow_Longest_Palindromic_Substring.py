class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        store = set()
        store.add("")
        res = None
        for i in s:
            store.add(i)
            res = i
        for ch in range(2, len(s)+1):
            for start in range(0, len(s)-ch+1):
                cur = s[start:start+ch]
                #print(cur)
                if cur[1:-1] in store and cur[0] == cur[-1]:
                    store.add(cur)
                    res = cur
        # max_len = 0
        # res = None
        # for i in store:
        #     if len(i) > max_len:
        #         max_len = len(i)
        #         res = i
        if res != None:
            return res
        else:
            return ""

a = Solution()
print(a.longestPalindrome("a"))