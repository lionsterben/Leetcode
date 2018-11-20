class Solution:
# @return a string
    def fractionToDecimal(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        stack = []
        sign = '-' if numerator*denominator < 0 else ''
        res = [sign+str(n), '.']
        while remainder not in stack:
            stack.append(remainder)
            n, remainder = divmod(remainder*10, abs(denominator))
            res.append(str(n))
        idx = stack.index(remainder)
        res.insert(idx+2,'(')
        res.append(')')
        return ''.join(res).replace('(0)',"").rstrip('.')