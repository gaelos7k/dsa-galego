// @ts-nocheck
var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        this.val = val;
        this.next = next;
    }
    return ListNode;
}());
function sortList(head) {
    return mergeSort(head);
}
function findMiddle(head) {
    var slow = head;
    var fast = head.next;
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    return slow;
}
function mergeTwoLists(l1, l2) {
    var dummy = new ListNode(0);
    var tail = dummy;
    while (l1 !== null && l2 !== null) {
        if (l1.val < l2.val) {
            tail.next = l1;
            l1 = l1.next;
        }
        else {
            tail.next = l2;
            l2 = l2.next;
        }
        tail = tail.next;
    }
    tail.next = l1 !== null ? l1 : l2;
    return dummy.next;
}
function mergeSort(head) {
    if (head === null || head.next === null) {
        return head;
    }
    var middle = findMiddle(head);
    var righHead = middle.next;
    middle.next = null;
    var left = mergeSort(head);
    var right = mergeSort(righHead);
    return mergeTwoLists(left, righHead);
}
console.log(typeof ListNode);
// Exemplo de uso do ListNode e sortList:
// Cria uma lista ligada: 4 -> 2 -> 1 -> 3
var n5 = new ListNode(3, null);
var n4 = new ListNode(1, n5);
var n3 = new ListNode(2, n4);
var n2 = new ListNode(4, n3);
var n1 = new ListNode(9, n2);
// Imprime a lista original
var curr = n1;
var originalOutput = "";
while (curr) {
    originalOutput += curr.val + (curr.next ? " -> " : "");
    curr = curr.next;
}
console.log("Lista original:", originalOutput);
// Ordena a lista
var sortedHead = sortList(n1);
// Imprime a lista ordenada
curr = sortedHead;
var sortedOutput = "";
while (curr) {
    sortedOutput += curr.val + (curr.next ? " -> " : "");
    curr = curr.next;
}
console.log("Lista ordenada:", sortedOutput);
