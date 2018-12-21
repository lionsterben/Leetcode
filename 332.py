from collections import defaultdict
class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        d = defaultdict(list)
        for flight in tickets:
            d[flight[0]] += flight[1],
        self.route = ["JFK"]
        def dfs(st):
            if len(self.route) == len(tickets)+1:
                return self.route
            dest = sorted(d[st])
            for sta in dest:
                d[st].remove(sta)
                self.route += sta,
                suc = dfs(sta)
                if suc:
                    return suc
                self.route.pop()
                d[st] += sta,
        return dfs("JFK")

## dfs + backtrack, 有效减少时间使用，相比于copy方式，多研究backtrack