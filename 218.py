class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        focus = []
        for bu in buildings:
            focus.append(bu[0])
            focus.append(bu[1])
        focus.sort()
        mask = {i:0 for i in focus}
        for bu in buildings:
            for idx in focus:
                if idx >= bu[0] and idx < bu[1]:
                    if bu[2] > mask[idx]:
                        mask[idx] = bu[2]
                if idx > bu[1]:
                    break
        res = [[focus[0], mask[focus[0]]]]
        temp = mask[focus[0]]
        for idx in focus:
            if mask[idx] == temp:
                continue
            if mask[idx] > temp:
                res.append([idx, mask[idx]])
            if mask[idx] < temp:
                res.append([idx, mask[idx]])
            temp = mask[idx]
        return res

##  right but TLE

from heapq import *

class Solution:
    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline
# 没太看懂，大致是当遇到新build，如果它的left在最高的right之前，先push进去，然后判断left这个点是否符合。如果left在最高点right之后，那么可以将这一个build pop出来了，还有right比它还小的build，这样
# 求出当前最高点的right和pop完之后有交集（right比这个大）的点。