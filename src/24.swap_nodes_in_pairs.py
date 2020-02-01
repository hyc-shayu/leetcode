from src.tool.struct import ListNode
from src.tool.test_data import getNodeList


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        cur = head
        tmpHead = ListNode(-1)
        tmpHead.next = head
        pre = tmpHead
        while cur and cur.next:
            pre.next = cur.next
            pre = cur
            right = cur.next
            # cur, cur.next, right.next = right.next, right.next, cur
            cur.next, right.next, cur = right.next, cur, right.next
        return tmpHead.next

    def swapPairs1(self, head):
        if head and head.next:
            nextNode = head.next
            head.next = self.swapPairs1(nextNode.next)
            nextNode.next = head
            return nextNode

        return head


if __name__ == '__main__':
    node = getNodeList()
    print(node.get_list())
    print((Solution().swapPairs1(node)).get_list())
