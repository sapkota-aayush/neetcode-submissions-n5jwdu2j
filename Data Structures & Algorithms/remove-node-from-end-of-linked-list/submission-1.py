class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current = head
        length = 0

        while current:
            length += 1
            current = current.next

        # handle case where we remove the head
        if n == length:
            return head.next

        current = head  # reset pointer (you used newNode but didn’t use it correctly)

        for _ in range(length - n - 1):
            current = current.next

        current.next = current.next.next

        return head