# Função principal do quicksort que recebe um array para ordenar
def quicksort(arr):
    # Função auxiliar que particiona o array e retorna o índice do pivô
    def partition(low, high):
        # Seleciona o último elemento como pivô
        pivot = arr[high]
        # Índice do menor elemento
        i = low - 1
        # Percorre o array do início até o pivô
        for j in range(low, high):
            # Se o elemento atual for menor ou igual ao pivô
            if arr[j] <= pivot:
                i += 1
                # Troca os elementos de posição
                arr[i], arr[j] = arr[j], arr[i]
        # Coloca o pivô na posição correta
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Função recursiva que implementa o quicksort
    def quicksort_recursive(low, high):
        if low < high:
            # Encontra a posição do pivô
            pi = partition(low, high)
            # Ordena recursivamente a parte esquerda
            quicksort_recursive(low, pi - 1)
            # Ordena recursivamente a parte direita
            quicksort_recursive(pi + 1, high)

    # Inicia a ordenação chamando a função recursiva
    quicksort_recursive(0, len(arr) - 1)
    return arr


# Array de teste
test_array = [10, 7, 8, 9, 1, 5]
# Imprime o array não ordenado
print("Unsorted array:", test_array)
# Ordena o array usando quicksort
sorted_array = quicksort(test_array)
# Imprime o array ordenado
print("Sorted array:", sorted_array)
