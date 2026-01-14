//@ts-nocheck
// Representa um nó da lista ligada, armazenando um valor e uma referência para o próximo nó.
// Essa estrutura é fundamental para listas ligadas, pois permite inserções e remoções eficientes.
class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val: number, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

// Função principal que inicia o processo de ordenação.
// Encapsula a chamada ao algoritmo Merge Sort, promovendo clareza e modularidade.
function sortList(head: ListNode | null): ListNode | null {
    return mergeSort(head);
}

// Encontra o nó do meio da lista usando dois ponteiros.
// Técnica eficiente que evita a contagem de elementos, ideal para listas ligadas.
function findMiddle(head: ListNode): ListNode {
    let slow: ListNode = head;
    let fast: ListNode | null = head.next;

    // O ponteiro 'fast' avança duas posições enquanto 'slow' avança uma.
    // Quando 'fast' chega ao final, 'slow' estará no meio.
    while (fast !== null && fast.next !== null) {
        slow = slow.next as ListNode;
        fast = fast.next.next;
    }

    return slow;
}

// Mescla duas listas ordenadas em uma única lista ordenada.
// Utiliza um nó auxiliar ('dummy') para simplificar a manipulação dos ponteiros.
function mergeTwoLists(
    l1: ListNode | null,
    l2: ListNode | null
): ListNode | null {
    const dummy = new ListNode(0);
    let tail = dummy;

    // Percorre ambas as listas, sempre escolhendo o menor elemento disponível.
    while (l1 !== null && l2 !== null) {
        if (l1.val < l2.val) {
            tail.next = l1;
            l1 = l1.next;
        } else {
            tail.next = l2;
            l2 = l2.next;
        }
        tail = tail.next;
    }

    // Ao final, conecta o restante da lista não esgotada.
    tail.next = l1 !== null ? l1 : l2;
    return dummy.next;
}

// Implementa o Merge Sort recursivo para listas ligadas.
// Divide a lista ao meio, ordena cada parte e mescla os resultados.
function mergeSort(head: ListNode | null): ListNode | null {
    // Caso base: lista vazia ou com apenas um elemento já está ordenada.
    if (head === null || head.next === null) {
        return head;
    }

    // Encontra o meio da lista para dividir em duas partes.
    const middle = findMiddle(head);
    const rightHead = middle.next;
    middle.next = null; // Separa as duas listas.

    // Ordena recursivamente cada metade.
    const left = mergeSort(head);
    const right = mergeSort(rightHead);

    // Mescla as duas listas ordenadas.
    return mergeTwoLists(left, right);
}
