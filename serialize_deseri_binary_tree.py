# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Codec:

        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        bfs = []
        q = Queue()
        q.put(root)
        bfs.append(root)
        while not q.empty():
            node = q.get()
            bfs.append(node.left)
            bfs.append(node.right)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        data = " ".join(str(x.val) if x is not None else '#' for x in bfs)
        return data
        
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        tmp = data.split(" ") 
        p = Queue()
        root = TreeNode(int(tmp[0]))
        p.put(root)
        cnt = 1
        print(data)
        # return None
        while not p.empty():
            node = p.get()
            left, right = tmp[cnt], tmp[cnt+1]
            cnt += 2
            if left != '#':
                nodeLeft = TreeNode(int(left))
                node.left = nodeLeft
                p.put(nodeLeft)
            if right != '#':
                nodeRight = TreeNode(int(right))
                node.right = nodeRight
                p.put(nodeRight)
        return root

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from queue import Queue
class Codec:

        
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        val = []
        def preorder(node):
            if node:
                val.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                val.append('#')
        preorder(root)
        return " ".join(val)

        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(" ")
        # print(data)
        vals = iter(data)
        def decode():
            nodeVal = next(vals)
            if nodeVal == '#':
                return None
            # print(nodeVal)
            node = TreeNode(int(nodeVal))
            node.left = decode()
            node.right = decode()
            return node
        return decode()