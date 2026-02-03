from typing import List  # Importa o tipo List para tipagem de listas aninhadas

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Cria um grafo representado por um dicionário, onde cada curso é uma chave e o valor é uma lista de cursos dependentes
        graph = {i: [] for i in range(numCourses)}
        # Preenche o grafo com as dependências dos cursos
        for a, b in prerequisites:
            graph[b].append(a)  # Para fazer o curso 'a', é necessário ter feito o curso 'b'

        # Cria uma lista para marcar o estado de cada nó: 0 = não visitado, 1 = visitando, 2 = visitado
        state = [0] * numCourses

        # Função auxiliar para detectar ciclos usando busca em profundidade (DFS)
        def has_cycle(v):
            if state[v] == 1:  # Se o nó está sendo visitado, há um ciclo
                return True
            if state[v] == 2:  # Se o nó já foi totalmente visitado, não há ciclo a partir dele
                return False

            state[v] = 1  # Marca o nó como 'visitando'
            for neighbor in graph[v]:  # Percorre todos os vizinhos (cursos dependentes)
                if has_cycle(neighbor):  # Se algum vizinho formar um ciclo, retorna True
                    return True
            state[v] = 2  # Marca o nó como 'visitado'
            return False  # Não encontrou ciclo a partir deste nó

        # Verifica todos os cursos para garantir que não há ciclos em nenhum componente do grafo
        for i in range(numCourses):
            if has_cycle(i):  # Se encontrar ciclo, não é possível terminar todos os cursos
                return False

        return True  # Se não encontrou ciclos, é possível terminar todos os cursos
