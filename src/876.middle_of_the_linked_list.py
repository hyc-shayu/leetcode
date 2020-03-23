from src.tool.struct import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode or None:
        if not head:
            return None
        mid = cur = head
        count = 1
        while cur.next:
            cur = cur.next
            count += 1
            if count & 1 == 0:
                mid = mid.next
        return mid
