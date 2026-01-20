# Classe Solution para compatibilidade com o driver
class Solution:
    def countBits(self, n: int) -> list:
        # Chama a função countingBits para calcular o número de bits 1
        return countingBits(n)

# 338. Counting Bits
# Dado um inteiro n, retorna um array ans de tamanho n+1 onde ans[i] é o número de bits 1 na representação binária de i
def countingBits(n: int) -> list:
    """
    Para cada i de 0 até n, calcula o número de bits 1 em i.
    Retorna uma lista ans onde ans[i] = número de bits 1 em i.
    Algoritmo O(n):
    Para cada i > 0, ans[i] = ans[i >> 1] + (i & 1)
    - i >> 1: desloca os bits de i para a direita (divide por 2), já calculado anteriormente
    - (i & 1): verifica se o último bit de i é 1 (par ou ímpar)
    """
    ans = [0] * (n + 1)  # Inicializa a lista de respostas com zeros
    for i in range(1, n + 1):
        # ans[i >> 1] já foi calculado, (i & 1) verifica se o último bit é 1
        # Exemplo: para i=5 (binário 101), i>>1=2 (binário 10), ans[2]=1, (5&1)=1, então ans[5]=1+1=2
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

# Exemplo de uso:
if __name__ == "__main__":
    # Para n=2, retorna [0, 1, 1]:
    # 0 -> 0b0 (0 bits 1)
    # 1 -> 0b1 (1 bit 1)
    # 2 -> 0b10 (1 bit 1)
    print(countingBits(2))  # Saída: [0, 1, 1]

    # Para n=5, retorna [0, 1, 1, 2, 1, 2]:
    # 0 -> 0b0 (0 bits 1)
    # 1 -> 0b1 (1 bit 1)
    # 2 -> 0b10 (1 bit 1)
    # 3 -> 0b11 (2 bits 1)
    # 4 -> 0b100 (1 bit 1)
    # 5 -> 0b101 (2 bits 1)
    print(countingBits(5))  # Saída: [0, 1, 1, 2, 1, 2]
