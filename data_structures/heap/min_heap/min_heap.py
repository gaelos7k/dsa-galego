class MinHeap:
    def __init__(self) -> None:
        # Inicializa o heap como uma lista vazia
        self.heap = []

    def _left_child(self, index):
        # Retorna o índice do filho à esquerda de um dado índice
        # Fórmula: 2 * índice + 1
        return 2 * index + 1

    def _right_child(self, index):
        # Retorna o índice do filho à direita de um dado índice
        # Fórmula: 2 * índice + 2
        return 2 * index + 2

    def _parent(self, index):
        # Retorna o índice do nó pai de um dado índice
        # Fórmula: (índice - 1) // 2 (divisão inteira)
        return (index - 1) // 2

    def _heapify_up(self, index):
        if index == 0:
            return  # O elemento já está na raiz, não há necessidade de subir

        parent_index = self._parent(index)

        if self.heap[index] < self.heap[parent_index]:
            # Troca o elemento atual com o pai
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Continua subindo o elemento para manter a propriedade do heap
            self._heapify_up(parent_index)
