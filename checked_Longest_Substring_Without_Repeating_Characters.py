class Solution(object):
                
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_str = {}
        start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] not in map_str or map_str[s[i]] < start:
                map_str[s[i]] = i
                # print(i)
                # print(s[i])
                # print(start)
                # print(map_str)
                if (i - start) + 1 > max_len:
                    max_len = i - start + 1
            else:
                temp = s[i]
                # print(i)
                # print(temp)
                start = map_str[s[i]] + 1
                map_str[s[i]] = i
        return max_len

a = Solution()
print(a.lengthOfLongestSubstring("aab"))
