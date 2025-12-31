from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        # Valor do nó
        self.val = val
        # Referência para o próximo nó
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Cria um nó fictício para facilitar a manipulação da lista resultante
        dummy = ListNode(0)
        # Ponteiro para construir a nova lista
        current = dummy

        # Percorre ambas as listas enquanto ambas não estiverem vazias
        while list1 and list2:
            # Compara os valores dos nós atuais de cada lista
            if list1.val < list2.val:
                # Adiciona o nó de list1 à lista resultante
                current.next = list1
                # Avança para o próximo nó em list1
                list1 = list1.next
            else:
                # Adiciona o nó de list2 à lista resultante
                current.next = list2
                # Avança para o próximo nó em list2
                list2 = list2.next
            # Avança o ponteiro da lista resultante
            current = current.next

        # Se ainda houver nós restantes em uma das listas, anexa-os ao final
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Retorna a lista mesclada, que começa após o nó fictício
        return dummy.next

# Exemplo de uso:
# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4
# merged: 1 -> 1 -> 2 -> 3 -> 4 -> 4
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Função para imprimir a lista ligada
def print_linked_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    print()
print_linked_list(merged_list)
