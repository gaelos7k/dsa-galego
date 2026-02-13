class ListNode:
    # Representa um nó da lista ligada, contendo um valor e a referência para o próximo nó
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMiddle(head):
    # Encontra o nó do meio da lista ligada usando dois ponteiros (técnica do rápido e lento)
    # Isso permite dividir a lista em duas partes aproximadamente iguais, essencial para o Merge Sort
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def mergeTwoLists(l1, l2):
    # Mescla duas listas ligadas ordenadas em uma única lista ordenada
    # Utiliza um nó sentinela para simplificar a lógica de inserção
    head = ListNode()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Ao final, apenas uma das listas pode ter elementos restantes; basta anexá-los
    tail.next = l1 or l2
    return head.next

def mergesort(head):
    # Ordena a lista ligada usando o algoritmo Merge Sort (dividir para conquistar)
    # Caso base: lista vazia ou com um único elemento já está ordenada
    if not head or not head.next:
        return head

    # Divide a lista ao meio
    middle = findMiddle(head)
    after_middle = middle.next
    middle.next = None  # Quebra a lista em duas partes

    # Ordena recursivamente cada metade
    left = mergesort(head)
    right = mergesort(after_middle)

    # Mescla as duas metades ordenadas
    return mergeTwoLists(left, right)

def buildLinkedList(values):
    # Constrói uma lista ligada a partir de uma lista de valores
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def printLinkedList(head):
    # Imprime os valores da lista ligada como uma lista Python
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)

# Exemplo de uso: cria uma lista ligada, ordena e imprime o resultado
values = [4, 2, 1, 3]
print("Unsorted Linked List:", values)
head = buildLinkedList(values)
sorted_head = mergesort(head)
print("Sorted Linked List:", end=" ")
printLinkedList(sorted_head)