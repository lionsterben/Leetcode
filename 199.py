#mine:
from queue import Queue
class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        qu = Queue()
        qu.put((root, 0))
        res = []
        while not qu.empty():
            node, mask = qu.get()
            if mask != 0 and mask != pre[1]:
                res.append(pre[0].val)
            pre = (node, mask)
            if node.left != None:
                qu.put((node.left, mask+1))
            if node.right != None:
                qu.put((node.right, mask+1))
            if qu.empty():
                res.append(node.val)
        return res

# elegant dfs solve
# public class Solution {
#     public List<Integer> rightSideView(TreeNode root) {
#         List<Integer> result = new ArrayList<Integer>();
#         rightView(root, result, 0);
#         return result;
#     }
    
#     public void rightView(TreeNode curr, List<Integer> result, int currDepth){
#         if(curr == null){
#             return;
#         }
#         if(currDepth == result.size()){
#             result.add(curr.val);
#         }
        
#         rightView(curr.right, result, currDepth + 1);
#         rightView(curr.left, result, currDepth + 1);
        
#     }
# }