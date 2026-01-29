from typing import Optional  # Importa o tipo Optional, que permite indicar que uma variável pode ser de um tipo específico ou None (nulo), promovendo clareza e segurança no código.
from collections import deque  # Importa deque, uma estrutura de dados eficiente para operações de inserção e remoção em ambas as extremidades, ideal para implementar filas (queues).

class Node:  # Define a classe Node, que representa um nó em um grafo.
    def __init__(self, val=0, neighbors=None):  # Método construtor, inicializa o nó com um valor e uma lista de vizinhos.
        self.val = val  # Atributo que armazena o valor do nó, útil para identificação ou armazenamento de dados.
        self.neighbors = neighbors if neighbors is not None else []  # Inicializa a lista de vizinhos; se não for fornecida, cria uma lista vazia, evitando o uso de listas mutáveis como valor padrão, o que pode causar bugs sutis.

class Solution:  # Define a classe Solution, que encapsula a solução para o problema de clonagem de grafos.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:  # Método principal, recebe um nó de entrada e retorna a raiz do grafo clonado.
        if not node:  # Verifica se o nó de entrada é None; caso seja, retorna None imediatamente, tratando o caso de grafo vazio.
            return node  # Retorna None, pois não há grafo a ser clonado.

        q = deque([node])  # Inicializa uma fila (deque) com o nó de entrada, que será usada para percorrer o grafo em largura (BFS).

        clones = {}  # Dicionário que irá mapear o valor de cada nó original para seu respectivo clone, garantindo que cada nó seja clonado apenas uma vez.
        clones[node.val] = Node(node.val, [])  # Cria o clone do nó inicial e armazena no dicionário, preparando para construir as conexões posteriormente.

        while q:  # Enquanto houver nós a serem processados na fila...
            curr = q.popleft()  # Remove o nó da frente da fila para processá-lo.
            curr_clone = clones[curr.val]  # Recupera o clone correspondente ao nó atual, garantindo que as conexões sejam feitas entre clones.

            for n in curr.neighbors:  # Percorre todos os vizinhos do nó atual.
                if n.val not in clones:  # Se o vizinho ainda não foi clonado...
                    clones[n.val] = Node(n.val, [])  # Cria o clone do vizinho e adiciona ao dicionário.
                    q.append(n)  # Adiciona o vizinho à fila para que seus vizinhos também sejam processados futuramente.

                curr_clone.neighbors.append(clones[n.val])  # Adiciona o clone do vizinho à lista de vizinhos do clone atual, replicando a estrutura do grafo original.

        return clones[node.val]  # Retorna o clone do nó inicial, que serve como raiz do grafo clonado.
