class Solution(object):
    def isUnique(self,str):
        n = len(str)
        i = 0
        while i != n:
            if str[i] in str[i + 1:]:
                return False
            i += 1
        return True
    
    def shit(self,s):
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        else:
            temp = self.shit(s[1:])
            length = len(temp)
            if s[1:].startswith(temp):
                if s[0] not in temp:
                    return s[0] + temp
                else:
                    return temp
            else:
                if self.isUnique(s[:length+1]):
                    return s[:length+1]
                elif self.isUnique(s[:length]):
                    return s[:length]
                else:
                    return temp
                
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(self.shit(s))
    
    
        
        