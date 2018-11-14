class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(s):
            cnt = 0
            for char in s:
                if char == "(":
                    cnt += 1
                if char == ")":
                    cnt -= 1
                if cnt < 0:
                    return False
            return cnt == 0
        st = {s}
        while True:
            valid = list(filter(isValid, st))
            if valid:
                return valid
            st = {pr[:ind]+pr[ind+1:] for pr in st for ind in range(len(pr))}
    
        
        