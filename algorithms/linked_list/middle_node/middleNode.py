class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Inicializa dois ponteiros: 'ahead' avança dois nós por vez, 'head' avança um nó por vez
        ahead = head

        # Enquanto 'ahead' não chegar ao final da lista
        while ahead and ahead.next:
            # 'ahead' avança dois nós
            ahead = ahead.next.next
            # 'head' avança um nó
            head = head.next

        # Quando 'ahead' chega ao final, 'head' estará no nó do meio
        return head