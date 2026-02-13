var ListNode = /** @class */ (function () {
    function ListNode(val, next) {
        this.val = val;
        this.next = next;
    }
    return ListNode;
}());
var n2 = new ListNode(2, null);
var n1 = new ListNode(4, n2);
var current = n1;
var output = "";
while (current) {
    output += "".concat(current.val, " -> ");
    current = current.next;
}
output += "null";
console.log(output);
