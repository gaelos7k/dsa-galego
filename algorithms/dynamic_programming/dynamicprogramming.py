class Solution:
    """
    Classe Solution com método numDecodings para calcular o número de maneiras de decodificar uma string numérica.
    Método:
        Calcula quantas maneiras diferentes a string 's', composta apenas por dígitos, pode ser decodificada em letras,
        considerando o mapeamento de '1' a 'A', '2' a 'B', ..., '26' a 'Z'. Retorna 0 se a string não pode ser decodificada.
    Parâmetros:
        s (str): String de dígitos a ser decodificada.
    Retorno:
        int: Número total de maneiras de decodificar a string.
    """
    def numDecodings(self, s: str) -> int:
        # Se a string está vazia ou começa com '0', não pode ser decodificada
        if not s or s[0] == '0':
            return 0

        n = len(s)  # Comprimento da string
        prev = 1    # Número de maneiras de decodificar até o caractere anterior ao anterior
        curr = 1    # Número de maneiras de decodificar até o caractere anterior

        # Itera sobre a string a partir do segundo caractere
        for i in range(1, n):
            temp = 0  # Variável temporária para armazenar o número de maneiras nesta posição

            # Se o caractere atual não é '0', pode ser decodificado sozinho
            if s[i] != '0':
                temp += curr
            
            # Verifica se os dois últimos caracteres formam um número válido entre 10 e 26
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                temp += prev

            # Atualiza os valores para a próxima iteração
            prev, curr = curr, temp

            # Se não há maneiras de decodificar até aqui, retorna 0
            if curr == 0:
                return 0

        # Retorna o número total de maneiras de decodificar a string
        return curr
