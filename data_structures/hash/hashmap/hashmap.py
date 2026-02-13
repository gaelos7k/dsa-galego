# Define uma classe chamada HashMap para implementar uma estrutura de dados de mapa de hash simples
class HashMap:
    # Método construtor para inicializar o mapa de hash com um tamanho dado (padrão 100)
    def __init__(self, size=100) -> None:
        self.size = size  # Armazena o tamanho do mapa de hash
        # Cria uma lista de listas vazias (baldes) para armazenar pares chave-valor
        self.buckets = [[] for _ in range(size)]

    # Método privado para calcular o índice de hash para uma chave dada
    def _hash(self, key):
        # Usa a função hash embutida do Python e módulo para ajustar ao intervalo dos baldes
        return hash(key) % self.size

    # Método para adicionar ou atualizar um par chave-valor no mapa de hash
    def put(self, key, value):
        index = self._hash(key)  # Obtém o índice do balde para a chave
        bucket = self.buckets[index]  # Acessa o balde correspondente

        # Itera pelo balde para verificar se a chave já existe
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Se a chave existe, atualiza seu valor e retorna
                bucket[i] = (key, value)
                return

        # Se a chave não existe, adiciona o novo par chave-valor ao balde
        bucket.append((key, value))

    # Método para recuperar o valor associado a uma chave dada
    def get(self, key):
        index = self._hash(key)  # Obtém o índice do balde para a chave
        bucket = self.buckets[index]  # Acessa o balde correspondente

        # Itera pelo balde para encontrar a chave
        for k, v in bucket:
            if k == key:
                # Se a chave for encontrada, retorna seu valor
                return v

        # Se a chave não for encontrada, retorna None
        return None

    # Método para remover um par chave-valor do mapa de hash
    def remove(self, key):
        index = self._hash(key)  # Obtém o índice do balde para a chave
        bucket = self.buckets[index]  # Acessa o balde correspondente

        # Itera pelo balde para encontrar a chave
        for i, (k, v) in enumerate(bucket):
            if k == key:
                # Se a chave for encontrada, deleta o par chave-valor do balde
                del bucket[i]
                return

    # Método para retornar uma representação em string do mapa de hash
    def __str__(self):
        # Cria uma lista de dicionários para cada balde não vazio e retorna como string
        return str([{k: v for k, v in bucket} for bucket in self.buckets if bucket])


# Cria uma instância de HashMap
hash_map = HashMap()

# Adiciona pares chave-valor ao mapa de hash
hash_map.put("augusto", 30)
hash_map.put("matheus", 25)
hash_map.put(17, ("cachorro", 13))

# Imprime a representação em string do mapa de hash
print(hash_map)

# Recupera e imprime o valor para a chave "augusto"
print(hash_map.get("augusto"))

# Remove a chave "augusto" do mapa de hash
hash_map.remove("augusto")

# Tenta recuperar e imprimir o valor para a chave "augusto" após a remoção
print(hash_map.get("augusto"))