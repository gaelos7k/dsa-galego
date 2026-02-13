from typing import List
#Import do List type in intern module

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ##inicializa a funcao com o array e o alvo como parametros
        baixo = 0
        ##primeiro ponteiro que comeca no primeiro item do vetor
        alto = len(nums)
        ##segundo ponteiro que comeca no ultimo item do vetor

        while baixo < alto:
            ##looping que executa enquanto os dois ponteiros não se encotrarem
            meio = int((alto + baixo) / 2)
            ##calcula o ponto medio entre os dois ponteiros

            if nums[meio] == target:
                return meio
            ##se o meio for o alvo, retorna o meio (que é o indice)
            elif nums[meio] < target:
                baixo = meio + 1
            ##se o meio for menor que o alvo, o ponteiro mais baixo assume a um valor adiante do meioo
            else:
                alto = meio
            ##se o meio for maior que o alvo, o ponteiro mais alto assume o valor do meio
        return -1
        