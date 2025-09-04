# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
        深さ優先で探索。
        leftrightがないノードが来たらsequenceに追加。
        最終seq1とseq2が一致するか判定してreturn
        """
        seq1=[]
        seq2=[]

        def dive(self,root,seq) -> list:
            if root.left is None and root.right is None:
                seq.append(root.val)
            
            if root.left:
                seq=dive(root.left,seq)
            
            if root.right:
                seq=dive(root.right,seq)

            return seq
        
        seq1=dive(root1,seq1)
        seq2=dive(root1,seq2)

        if seq1==seq2:
            return True
        return False