from heapq import *
class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []
    
    # def binarySearch(self, l, r, target):
    #     while l < r:
    #         mid = (l+r)//2
    #         if self.data[mid] < target:
    #             l = mid+1
    #         else:
    #             r = mid
    #     return l
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        # heappush(self.small, -heappushpop(self.large, num))
        # if len(self.small) > len(self.large):
        #     heappush(self.large, -heappop(self.small))
        # heappush(self.small, -heappushpop(self.large, num))
        heappush(self.large, -heappushpop(self.small, -num))
        if len(self.small)+2 == len(self.large):
            heappush(self.small, -heappop(self.large))
        
        
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.large) > len(self.small):
            return float(self.large[0])
        return (self.large[0]-self.small[0])/2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()