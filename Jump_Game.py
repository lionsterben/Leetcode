class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastInd = len(nums) - 1
        res = {}
        def jump(ind):
            # print(ind)
            if ind == lastInd:
                return True
            if ind > lastInd:
                return False
            if nums[ind] == 0:
                return False
            # validStep = min()
            for step in reversed(range(1, nums[ind]+1)):
                # print(step)
                if ind + step in res:
                    if res[ind+step]:
                        return True
                else:
                    if jump(ind+step):
                        res[ind+step] = True
                        return True
                    else:
                        res[ind+step] = False
            return False
        return jump(0)

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastInd = len(nums) - 1
        res = []
        for i in range(lastInd):
            res.append(False)
        res.append(True)
        for i in reversed(range(lastInd)):
            jump = min(i+nums[i], lastInd)
            for j in range(i+1, jump+1):
                if res[j]:
                    res[i] = True
                    break
        
        
        return res[0]

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        lastPos = len(nums) - 1
        for i in reversed(range(len(nums)-1)):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0