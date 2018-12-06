class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        res = [0 for _ in range(m+n)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                cc = int(num1[i])*int(num2[j])
                p1, p2 = i+j, i+j+1
                cur = cc + res[p2]
                res[p2] = cur%10
                res[p1] += cur//10
        hehe = ""
        for i in range(len(res)):
            if not(res[i] == 0 and hehe==""):
                hehe += str(res[i])
        return hehe if hehe != "" else "0"
            