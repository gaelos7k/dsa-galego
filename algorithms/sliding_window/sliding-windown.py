class Solution:
    # Função que encontra o tamanho máximo de uma substring onde cada caractere aparece no máximo 2 vezes
    def maximumLengthSubstring(self, s: str) -> int:
        # Inicializa dois ponteiros - r (direita) e l (esquerda) no início da string
        r, l = 0, 0
        # Inicializa o tamanho máximo como 1 (menor substring possível)
        _max = 1
        # Dicionário para contar a frequência de cada caractere
        counter = {}

        # Adiciona o primeiro caractere ao contador
        counter[s[0]] = 1

        # Loop enquanto o ponteiro direito não chegar ao final da string
        while r < len(s) - 1:
            # Move o ponteiro direito
            r+=1
            # Se o caractere já existe no contador, incrementa sua contagem
            if counter.get(s[r]):
                counter[s[r]] += 1
            # Se é um novo caractere, inicia sua contagem como 1
            else:
                counter[s[r]] = 1
            
            # Se um caractere aparece 3 vezes, move o ponteiro esquerdo até resolver
            while counter[s[r]] == 3:
                # Diminui a contagem do caractere na posição do ponteiro esquerdo
                counter[s[l]] -= 1
                # Move o ponteiro esquerdo
                l+=1
            # Atualiza o tamanho máximo comparando com a diferença atual entre os ponteiros
            _max = max(_max, r-l+1)
        # Retorna o tamanho máximo encontrado
        return _max
