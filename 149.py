# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b
import numpy
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        res = 0
        for i in range(len(points)):
            same = 0
            mem = {'inf':1}
            # mem = {}
            for j in range(i+1, len(points)):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    same += 1
                    continue
                if points[i].x == points[j].x:
                    slope = 'inf'
                else:
                    slope = numpy.float128((points[i].y - points[j].y))/numpy.float128((points[i].x - points[j].x))
                if slope not in mem:
                    mem[slope] = 2
                else:
                    mem[slope] += 1
            print(mem)
            res = max(res, max(mem.values())+same)     

        return res