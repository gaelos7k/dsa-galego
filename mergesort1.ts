//@ts-nocheck

//Representa um nó de uma linked list
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null) {
    this.val = val;
    this.next = next;
  }
}

//Encapsula merge sort
function sortList(head: ListNode | null): ListNode | null {
  return mergeSort(head);
}

// Encontra o meio da linked list usando dois ponteiros
function findMiddle(head: ListNode): ListNode {
  let slow: ListNode = head;
  let fast: ListNode | null = head.next;

  // ponteiro slow avança 1, fast 2
  // fast quando tiver no final slow vai ta no meio
  while (fast !== null && fast.next !== null) {
    slow = slow.next as ListNode;
    fast = fast.next.next;
  }

  return slow;
}

//Mergea duas linked list
//dummy é um node auxiliar
function mergeTwoLists(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;

  // percorre ambas listas ate chegar o final de uma delas
  while (l1 !== null && l2 !== null) {
    if (l1.val < l2.val){
      tail.next = l1;
      l1 = l1.next; 
    } else {
      tail.next = l2;
      l2 = l2.next;
    }
    tail = tail.next;
  }

  // Conecta a lista que faltou percorrer até o final, no final.
  tail.next = l1 !== null ? l1 : l2;
  return dummy.next
}


//Implementa merge sort para linkedlist
//Divide a lista no meio, ordena cada parte e mergea o resultado
function mergeSort(head: ListNode | null): ListNode | null {
  // Caso base (lista vazia ou com um elemento já está ordenada)
  if (head === null || head.next === null) {
    return head;
  }

    //Encontra o meio da lista para dividir em duas partes
    const middle = findMiddle(head);
    const rightHead = middle.next;
    middle.next = null // Separa as duas listas

    // Ordenas recursivamente
    const left = mergeSort(head);
    const right = mergeSort(rightHead);

    // Mergea as duas listas ordenadas
    return mergeTwoLists(left, right);
}