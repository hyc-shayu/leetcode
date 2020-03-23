from src.tool.struct import ListNode
from src.tool.test_data import get_rand_node_list


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        tmp_head = ListNode(-1)
        tmp_head.next = head
        pre = tmp_head
        while cur and cur.next:
            pre.next = cur.next
            pre = cur
            right = cur.next
            # cur, cur.next, right.next = right.next, right.next, cur
            cur.next, right.next, cur = right.next, cur, right.next
        return tmp_head.next

    def swapPairs1(self, head):
        if head and head.next:
            next_node = head.next
            head.next = self.swapPairs1(next_node.next)
            next_node.next = head
            return next_node

        return head


if __name__ == '__main__':
    node = get_rand_node_list()
    print(node.get_list())
    print((Solution().swapPairs1(node)).get_list())
