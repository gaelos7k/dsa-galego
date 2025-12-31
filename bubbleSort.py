def bubble_sort(arr):
    # Obtém o tamanho do array
    tamanhoArr = len(arr)
    # Percorre todos os elementos do array
    for i in range(tamanhoArr):
        # Os últimos i elementos já estão ordenados
        for j in range(0, tamanhoArr - i - 1):
            # Compara elementos adjacentes
            if arr[j] > arr[j + 1]:
                # Troca se o elemento atual for maior que o próximo
                arr[j], arr[j + 1] = arr[j + 1], arr[j]