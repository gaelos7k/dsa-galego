
from typing import List


class Solution:
    # Define o método missingNumber que recebe uma lista de inteiros
    def missingNumber(self, nums: List[int]) -> int:
        x = 0  # Inicializa a variável x com 0
        for num in nums:  # Percorre cada número na lista nums
            x ^= num  # Aplica o operador XOR entre x e o número atual
        for i in range(len(nums)+1):  # Percorre todos os números de 0 até n (inclusive)
            x ^= i  # Aplica o operador XOR entre x e o índice atual
        return x  # Retorna o valor de x, que é o número que está faltando
