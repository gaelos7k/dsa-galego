class Stack:  # Define uma classe chamada Stack
    def __init__(self, max_length=1000):  # Construtor com parâmetro opcional max_length
        self.items = [0] * max_length  # Inicializa a pilha com uma lista de tamanho fixo
        self.max_length = max_length  # Armazena o tamanho máximo da pilha
        self.pointer = 0  # Ponteiro para rastrear o topo da pilha

    def push(self, item):  # Método para adicionar um item à pilha
        if self.pointer >= self.max_length:  # Verifica se ocorreu overflow
            raise IndexError("Stack overflow")  # Lança erro se a pilha estiver cheia
        self.items[self.pointer] = item  # Coloca o item na posição do topo
        self.pointer += 1  # Move o ponteiro para cima

    def pop(self):  # Método para remover e retornar o item do topo
        if self.pointer == 0:  # Verifica se a pilha está vazia
            raise IndexError("Empty stack")  # Lança erro se a pilha estiver vazia
        self.pointer -= 1  # Move o ponteiro para baixo
        return self.items[self.pointer]  # Retorna o item na nova posição do topo

    def peek(self):  # Método para visualizar o item do topo sem removê-lo
        if self.pointer == 0:  # Verifica se a pilha está vazia
            raise IndexError("Empty stack")  # Lança erro se a pilha estiver vazia
        return self.items[self.pointer - 1]  # Retorna o item no topo

    def size(self):  # Método para obter o tamanho atual da pilha
        return self.pointer  # Retorna o número de itens na pilha