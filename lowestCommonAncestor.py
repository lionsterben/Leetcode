# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isInTree(self,node, p):
        # print(node.val)
        # print(p)
        if node == None:
            return False
        if node.val == p:
            return True
        return self.isInTree(node.left,p) or self.isInTree(node.right,p)
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lca(root, p.val, q.val)
        
    def lca(self, node, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if node.val == p or node.val == q:
            return node
        left_p = self.isInTree(node.left,p)
        right_p = not left_p
        left_q = self.isInTree(node.left,q)
        right_q = not left_q
        # print(left_p,left_q)
        if (left_p and right_q) or (left_q and right_p):
            return node
        if left_p and left_q:
            return self.lca(node.left, p, q)
        if right_p and right_q:
            return self.lca(node.right, p, q)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def path(self, node):
        path = {}
        mark = []
        # print(11)
        def PathTree(node):
            # print(node.val)
            # print(p)
            if node == None:
                return
            mark.append(node.val)
            if node.left != None and node.left.val not in mark:
                path[node.left.val] = node.val
                PathTree(node.left)
            if node.right != None and node.right.val not in mark:
                path[node.right.val] = node.val
                PathTree(node.right)
        PathTree(node)
        return path
        
            
    def dfs(self,node, val):
        if node == None:
            return None
        if node.val == val:
            return node
        d = self.dfs(node.left, val)
        if d != None:
            return d
        f = self.dfs(node.right, val)
        if f != None:
            return f
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path = self.path(root)
        # print(path)
        # return self.lca(root, p.val, q.val)
        p_path = []
        q_path = []
        start_p = p.val
        start_q = q.val
        # print(path)
        while(start_p != root.val):
            p_path.append(start_p)
            start_p = path[start_p]
        while(start_q != root.val):
            q_path.append(start_q)
            start_q = path[start_q]
        p_path.append(root.val)
        q_path.append(root.val)
        # print(p_path)
        # print(q_path)
        res = -1
        for i in p_path:
            if i in q_path:
                res = i
                break
        # print(res)
        return self.dfs(root, res)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    dp = {}
    def isInTree(self,node, p):
        # print(node.val)
        # print(p)
        if node == None:
            return False
        if node.val == p:
            self.dp[(node,p)] = True
            return True
        if (node.left,p) in self.dp:
            left = self.dp[(node.left,p)]
        else:
            left = self.isInTree(node.left,p)
            self.dp[(node.left,p)] = left
        if (node.right,p) in self.dp:
            right = self.dp[(node.right,p)]
        else:
            right = self.isInTree(node.right,p)
            self.dp[(node.right,p)] = right
        return left or right
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lca(root, p.val, q.val)
        
    def lca(self, node, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if node.val == p or node.val == q:
            return node
        left_p = self.isInTree(node.left,p)
        right_p = not left_p
        left_q = self.isInTree(node.left,q)
        right_q = not left_q
        # print(left_p,left_q)
        if (left_p and right_q) or (left_q and right_p):
            return node
        if left_p and left_q:
            return self.lca(node.left, p, q)
        if right_p and right_q:
            return self.lca(node.right, p, q)