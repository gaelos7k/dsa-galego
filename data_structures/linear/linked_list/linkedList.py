class Node:
    # Representa um nó da lista duplamente ligada
    def __init__(self, value):
        self.value = value  # Valor armazenado no nó
        self.next = None    # Referência para o próximo nó
        self.prev = None    # Referência para o nó anterior



class DoublyLinkedList:
    # Implementa uma lista duplamente ligada
    def __init__(self):
        self.head = None  # Primeiro nó da lista
        self.tail = None  # Último nó da lista

    def add_to_front(self, value):
        """Adiciona um novo nó no início da lista."""
        new_node = Node(value)
        if not self.head:
            # Se a lista está vazia, head e tail apontam para o novo nó
            self.head = self.tail = new_node
        else:
            # Liga o novo nó ao início da lista
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        """Adiciona um novo nó no final da lista."""
        new_node = Node(value)
        if not self.tail:
            # Se a lista está vazia, head e tail apontam para o novo nó
            self.head = self.tail = new_node
        else:
            # Liga o novo nó ao final da lista
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        """Remove e retorna o valor do primeiro nó da lista."""
        if not self.head:
            # Lista vazia
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            # Só há um elemento na lista
            self.head = self.tail = None
        else:
            # Remove o primeiro nó e atualiza o head
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        """Remove e retorna o valor do último nó da lista."""
        if not self.tail:
            # Lista vazia
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            # Só há um elemento na lista
            self.head = self.tail = None
        else:
            # Remove o último nó e atualiza o tail
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value
