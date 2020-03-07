from src.tool.struct import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        if l1.val > l2.val:
            l1, l2 = l2, l1
        head = l1
        pre = None
        while l1 and l2:
            while l1 and l1.val <= l2.val:
                pre = l1
                l1 = l1.next
            pre.next = l2
            l1, l2 = l2, l1

        return head


if __name__ == '__main__':
    node1_1 = ListNode(1)
    node1_2 = ListNode(1)
    node1_1.next = node1_2

    node2_1 = ListNode(3)
    node2_2 = ListNode(6)
    node2_1.next = node2_2
    node2_3 = ListNode(9)
    node2_2.next = node2_3

    obj = Solution()

    print(obj.mergeTwoLists(node1_1, node2_1))
