from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dicionário para armazenar o último índice de cada número
        last_index = {}
        # Percorre o array com índice e valor
        for i, num in enumerate(nums):
            # Se o número já apareceu antes
            if num in last_index:
                # Verifica se a diferença de índices é menor ou igual a k
                if i - last_index[num] <= k:
                    return True  # Encontrou duplicado próximo
            # Atualiza o último índice do número
            last_index[num] = i
        # Se não encontrou nenhum duplicado próximo
        return False