class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        forge = sorted(heights)
        res = 0
        for i in forge:
            start, end = 0, 0
            for ind in range(len(heights)):
                if heights[ind] >= i:
                    end += 1
                if heights[ind] < i or ind == len(heights) - 1:
                    res = max(res, (end-start)*i)
                    start = end + 1
                    end = end + 1
        return res

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        area = 0
        ind = 0
        while ind < len(heights):
            h = heights[ind]
            if not stack or h >= heights[stack[-1]]:
                stack.append(ind)
                ind += 1
            else:
                smallestBar = stack.pop()
                if stack:
                    curArea = heights[smallestBar] * (ind-stack[-1]-1)
                else:
                    curArea = heights[smallestBar] * ind
                if curArea > area:
                    area = curArea
        while stack:
            cur = stack.pop()
            if stack:
                curArea = heights[cur] * (ind-stack[-1]-1)
            else:
                curArea = heights[cur] * ind
            if curArea > area:
                area = curArea
        return area