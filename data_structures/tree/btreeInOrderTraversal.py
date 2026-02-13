# Importa os tipos List e Optional para anotações de tipo
from typing import List, Optional

# Define a classe TreeNode para representar um nó de uma árvore binária


class TreeNode:
    # O construtor recebe o valor do nó e, opcionalmente, os filhos esquerdo e direito
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val  # Armazena o valor do nó
        self.left = left  # Referência para o filho à esquerda (pode ser None)
        self.right = right  # Referência para o filho à direita (pode ser None)


class Solution:
    # Define o método inorderTraversal que recebe a raiz da árvore binária
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Função auxiliar recursiva para percorrer a árvore em ordem
        def inorder(root):
            # Se o nó não for None, percorre a subárvore esquerda, visita o nó atual e percorre a subárvore direita
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []
            # Se o nó for None, retorna uma lista vazia (caso base da recursão)

        # Chama a função auxiliar passando a raiz e retorna o resultado
        return inorder(root)
