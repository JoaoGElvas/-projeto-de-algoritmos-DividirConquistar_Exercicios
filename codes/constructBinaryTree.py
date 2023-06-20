from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Obtenha o valor raiz (primeiro elemento)
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Encontra o índice do valor raiz na não ordenada
        root_idx = inorder.index(root_val)
        
        # Constroi as subárvores da esquerda e da direita recursivamente
        root.left = self.buildTree(preorder[1:root_idx+1], inorder[:root_idx])
        root.right = self.buildTree(preorder[root_idx+1:], inorder[root_idx+1:])
        
        return root
