class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Inicializa um nó da árvore binária com valor, filho esquerdo e direito
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # Se uma das listas estiver vazia, não há árvore para construir
        if not inorder or not postorder:
            return None

        # O último elemento do postorder é sempre a raiz da árvore/subárvore
        root = TreeNode(postorder.pop())

        # Encontra o índice da raiz no inorder para separar subárvore esquerda e direita
        inorder_index = inorder.index(root.val)

        # Constrói recursivamente a subárvore direita primeiro, pois estamos consumindo postorder de trás pra frente
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)

        # Depois constrói a subárvore esquerda
        root.left = self.buildTree(inorder[:inorder_index], postorder)

        # Retorna o nó raiz da árvore/subárvore construída
        return root
