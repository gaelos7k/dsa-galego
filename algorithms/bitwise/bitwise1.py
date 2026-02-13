# Classe Solution para compatibilidade com o driver
class Solution:
	def hammingWeight(self, n: int) -> int:
		return hamming_weight(n)
# Peso de Hamming: Conta o número de bits 1 na representação binária de n
def hamming_weight(n: int) -> int:
	"""
	Retorna o número de bits 1 na representação binária de n.
	Exemplo: n = 11 (0b1011) -> retorna 3
	"""
	count = 0
	while n:
		# n & (n - 1) remove o bit 1 menos significativo
		n &= n - 1
		count += 1
	return count

# Exemplo de uso:
if __name__ == "__main__":
	print(hamming_weight(11))         # Saída: 3
	print(hamming_weight(128))        # Saída: 1
	print(hamming_weight(2147483645)) # Saída: 30

# Observação de otimização:
# Se esta função for chamada muitas vezes, considere pré-calcular o peso de Hamming para todos os valores possíveis de byte (0-255)
# e usar uma tabela de consulta para processar n em blocos (por exemplo, 8 bits por vez) para resultados mais rápidos.
