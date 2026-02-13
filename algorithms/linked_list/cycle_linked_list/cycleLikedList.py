class Solution:
    # Checa se a linked list tem um ciclo
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Inicializa ponteiros
        slow = head
        fast = head

        #enquanto fast existir e tiver algo em sua frente
        while fast and fast.next:
            #ponteiro lento anda 1, ponteiro rapido anda duas casas
            slow = slow.next
            fast = fast.next.next
            #se lento = rapido entao o ciclo existe, retorna verdadeiro, se nao retorna falso
            if slow == fast:
                return True
        return False
