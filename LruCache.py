
# Classe que representa um nó da lista duplamente ligada
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value  # Armazena chave e valor
        self.prev, self.next = None, None  # Ponteiros para o nó anterior e próximo



# Classe que implementa o LRU Cache
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity  # Capacidade máxima do cache
        self.cache = {}  # Dicionário para mapear chave -> nó

        # Nós sentinelas para facilitar inserção e remoção
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left  # Inicializa lista vazia

    # Remove um nó da lista duplamente ligada
    def remove(self, node):
        prev, _next = node.prev, node.next  # Nó anterior e próximo
        prev.next = _next  # Liga anterior ao próximo
        _next.prev = prev  # Liga próximo ao anterior

    # Insere um nó logo após o sentinela da esquerda (mais recente)
    def insert(self, node):
        prev, _next = self.left, self.left.next  # Nó sentinela e o primeiro real
        prev.next = _next.prev = node  # Liga sentinela e primeiro real ao novo nó
        node.next = _next  # Próximo do novo nó é o antigo primeiro
        node.prev = prev  # Anterior do novo nó é o sentinela

    # Retorna o valor associado à chave, se existir, e atualiza como mais recente
    def get(self, key: int) -> int:
        if key in self.cache:  # Se a chave existe
            self.remove(self.cache[key])  # Remove da posição atual
            self.insert(self.cache[key])  # Insere como mais recente
            return self.cache[key].value  # Retorna o valor
        return -1  # Se não existe, retorna -1

    # Adiciona ou atualiza um par chave-valor no cache
    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # Se a chave já existe
            self.remove(self.cache[key])  # Remove o nó antigo
        self.cache[key] = Node(key, value)  # Cria novo nó e adiciona ao dicionário
        self.insert(self.cache[key])  # Insere como mais recente

        if len(self.cache) > self.capacity:  # Se excedeu a capacidade
            lru = self.right.prev  # Nó menos recentemente usado (antes do sentinela direito)
            self.remove(lru)  # Remove da lista
            del self.cache[lru.key]  # Remove do dicionário
