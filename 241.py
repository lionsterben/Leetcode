class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for idx in range(len(input)):
            if input[idx] in "+-*":
                res_1 = self.diffWaysToCompute(input[:idx])
                res_2 = self.diffWaysToCompute(input[idx+1:])
                for i in res_1:
                    for j in res_2:
                        res.append(self.cal(i,j,input[idx]))
        return res
    
    def cal(self,num1, num2, op):
        if op == "-":
            return num1-num2
        elif op == "*":
            return num1*num2
        else:
            return num1+num2