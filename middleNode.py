class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ahead = head

        while ahead and ahead.next:
            ahead = ahead.next.next
            head = head.next

        return head