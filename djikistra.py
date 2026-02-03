import heapq  # Importa a biblioteca para usar a fila de prioridade (heap)
from typing import List  # Importa List para tipagem de listas aninhadas

class Solution:
    # Função para calcular o tempo mínimo para todos os nós receberem o sinal
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        table = {}  # Dicionário para armazenar o grafo como lista de adjacência

        # Constrói a lista de adjacência a partir da lista de arestas
        for t in times:
            # Se o nó de origem ainda não está na tabela, cria um novo dicionário para ele
            if not table.get(t[0]):
                table[t[0]] = {t[1]: t[2]}
            else:
                # Se já existe, adiciona/atualiza o nó de destino e o peso
                table[t[0]][t[1]] = t[2]

        distances = {k: 0}  # Dicionário para armazenar a menor distância conhecida até cada nó, começa pelo nó inicial k

        min_heap = [(0, k)]  # Fila de prioridade (heap) iniciando pelo nó k com distância 0

        # Enquanto houver nós para processar na fila de prioridade
        while min_heap:
            dist, node = heapq.heappop(min_heap)  # Remove o nó com menor distância acumulada

            row = table.get(node)  # Obtém os vizinhos do nó atual

            if row:
                # Para cada vizinho do nó atual
                for key, v in row.items():
                    table_dist = distances.get(key, float('inf'))  # Distância conhecida até o vizinho
                    # Se encontrar um caminho mais curto até o vizinho, atualiza
                    if dist + v < table_dist:
                        distances[key] = dist + v
                        heapq.heappush(min_heap, (dist + v, key))  # Adiciona o vizinho na fila de prioridade

        _max = -1  # Variável para armazenar o maior tempo de chegada do sinal
        if len(distances) < n:
            return _max  # Se nem todos os nós foram alcançados, retorna -1

        # Calcula o maior tempo entre todos os nós alcançados
        for key, v in distances.items():
            _max = max(_max, v)

        if _max == 0:
            return -1  # Se o maior tempo for 0, significa que não foi possível alcançar todos os nós

        return _max  # Retorna o tempo mínimo necessário para que todos recebam o sinal