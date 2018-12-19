class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        gp = {i:[] for i in range(n)}
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            gp[node1].append(node2)
            gp[node2].append(node1)
        def get_min(node):
            height = []
            mask = [0 for _ in range(n)]
            def dfs(node, h):
                flag = True
                if gp[node]:
                    for i in gp[node]:
                        flag = flag and mask[i]
                if flag:
                    height.append(h)
                    return
                mask[node] = 1
                for child in gp[node]:
                    if not mask[child]:
                        dfs(child, h+1)
            dfs(node,0)
            return max(height)
        res = [get_min(node) for node in range(n)]
        mind = min(res)
        cc = []
        for i in range(len(res)):
            if res[i] == mind:
                cc.append(i)
        return cc

## 有点蠢的做法，O(n2)，TLE

class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        gp = {i:[] for i in range(n)}
        for edge in edges:
            node1, node2 = edge[0], edge[1]
            gp[node1].append(node2)
            gp[node2].append(node1)
        leave = [node for node in range(n) if len(gp[node])==1]
        while n > 2:
            n -= len(leave)
            new_leave = []
            for node in leave:
                ver = gp[node][0]
                gp[ver].remove(node)
                if len(gp[ver])==1:
                    new_leave.append(ver)
            leave = new_leave
        return leave

## 不断去除叶节点，利用bfs找到最后一个或者两个节点，意思是最长的路径的中间节点。