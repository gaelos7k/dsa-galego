from typing import List  # Importa o tipo List para tipagem dos parâmetros

class Solution:  # Define a classe Solution
    def numIslands(self, grid: List[List[str]]) -> int:  # Método que recebe uma matriz de caracteres e retorna um inteiro
        if not grid:  # Verifica se a matriz está vazia
            return 0  # Se estiver vazia, retorna 0 (nenhuma ilha)

        m, n = len(grid), len(grid[0])  # m: número de linhas, n: número de colunas da matriz
        count = 0  # Inicializa o contador de ilhas encontradas

        def dfs(i, j):  # Função auxiliar para busca em profundidade (DFS)
            # Verifica se o índice está fora dos limites ou se a célula não é terra ('1')
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return  # Sai da função se não for possível continuar

            grid[i][j] = '0'  # Marca a célula como visitada, alterando para água ('0')

            dfs(i+1, j)  # Chama DFS para a célula abaixo
            dfs(i-1, j)  # Chama DFS para a célula acima
            dfs(i, j+1)  # Chama DFS para a célula à direita
            dfs(i, j-1)  # Chama DFS para a célula à esquerda

        # Percorre todas as células da matriz
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # Se encontrar terra ('1')
                    count += 1  # Incrementa o contador de ilhas
                    dfs(i, j)  # Executa DFS para marcar toda a ilha como visitada

        return count  # Retorna o número total de ilhas encontradas
