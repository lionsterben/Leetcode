from collections import defaultdict
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        def isOverlap(s1, s2):
            return (s1.end > s2.start and s1.start < s2.end) or (s2.end > s1.start and s2.start < s1.end)
        
        graph = defaultdict(list)
        
        ## use idx to key
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                if isOverlap(intervals[i], intervals[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        print(graph)
        
        def judge(a):
            for i in a:
                if i:
                    return False
            return True
        cnt = 0
        
        while not judge(graph.values()):
            max_idx, max_val = 0, 0
            for k,v in graph.items():
                if len(v) > max_val:
                    max_val = len(v)
                    max_idx = k
            graph[max_idx] = []
            for k in graph:
                if max_idx in graph[k]:
                    graph[k].remove(max_idx)
            cnt += 1
        return cnt
            
## wrong solution, 抽象成图之后，贪心解决丢失了某些信息


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        end = float("-inf")
        erase = 0
        for interval in sorted(intervals, key=lambda i: i.end):
            if interval.start >= end:
                end = interval.end
            else:
                erase += 1
        return erase

## 贪心算法