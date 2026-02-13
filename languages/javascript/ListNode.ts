class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null) {
    this.val = val;
    this.next = next;
  }
}

const n2 = new ListNode(2, null);
const n1 = new ListNode(4, n2);

let current: ListNode | null = n1;
let output = "";

while (current) {
  output += `${current.val} -> `;
  current = current.next;
}

output += "null";
console.log(output);
