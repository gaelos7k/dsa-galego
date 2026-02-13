// @ts-nocheck

class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null) {
    this.val = val;
    this.next = next;
  }
}

function sortList(head: ListNode | null): ListNode | null {
  return mergeSort(head);
}

function findMiddle(head: ListNode): listNode {
  let slow: ListNode = head;
  let fast: ListNode | null = head.next;

  while (fast !== null && fast.next !== null) {
    slow = slow.next as ListNode;
    fast = fast.next.next;
  }
  return slow;
}

function mergeTwoLists(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;

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

  tail.next = l1 !== null ? l1 : l2;
  return dummy.next;
}

function mergeSort(head: ListNode | null): ListNode | null {
  if (head === null || head.next === null) {
    return head;
  }

  const middle = findMiddle(head);
  const righHead = middle.next;
  middle.next = null;

  const left = mergeSort(head);
  const right = mergeSort(righHead);

  return mergeTwoLists(left, righHead);
}

console.log(typeof ListNode);

// Exemplo de uso do ListNode e sortList:

// Cria uma lista ligada: 9 -> 4 -> 2 -> 1 -> 3
const n5 = new ListNode(3, null);
const n4 = new ListNode(1, n5);
const n3 = new ListNode(2, n4);
const n2 = new ListNode(4, n3);
const n1 = new ListNode(9, n2);

// Imprime a lista original
let curr = n1;
let originalOutput = "";
while (curr) {
    originalOutput += curr.val + (curr.next ? " -> " : "");
    curr = curr.next;
}
console.log("Lista original:", originalOutput);

// Ordena a lista
const sortedHead = sortList(n1);

// Imprime a lista ordenada
curr = sortedHead;
let sortedOutput = "";
while (curr) {
    sortedOutput += curr.val + (curr.next ? " -> " : "");
    curr = curr.next;
}
console.log("Lista ordenada:", sortedOutput);
