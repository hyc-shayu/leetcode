from src.tool.struct import ListNode
from src.tool.test_data import get_node_list


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode or None:
        if not head:
            return None
        my_head = ListNode(0)
        my_head.next = head
        prev = my_head
        cur = head
        dup_val = None

        while cur:
            if cur.val == dup_val:
                cur = cur.next
                continue
            if cur.next and cur.val == cur.next.val:
                dup_val = cur.val
                cur = cur.next.next
                continue
            prev.next = cur
            prev = cur
            cur = cur.next

        prev.next = None

        return my_head.next


if __name__ == '__main__':
    s = Solution()
    node = get_node_list([1, 2, 3, 3, 4, 4, 5])
    s.deleteDuplicates(node)
