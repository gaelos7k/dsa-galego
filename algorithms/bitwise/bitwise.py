class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0  # Inicializa o contador de passos como zero
        while num > 0:  # Continua enquanto o número for maior que zero
            if num & 1:  # Verifica se o número é ímpar (último bit é 1)
                num -= 1  # Se for ímpar, subtrai 1
            else:
                num >>= 1  # Se for par, divide por 2 usando deslocamento de bits
            steps += 1  # Incrementa o contador de passos
        return steps  # Retorna o número total de passos