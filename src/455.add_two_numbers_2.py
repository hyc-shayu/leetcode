from src.tool.struct import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        if l2.val == 0:
            return l1

        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        node = None
        while stack1 or stack2 or carry != 0:
            a = stack1.pop() if stack1 else 0
            b = stack2.pop() if stack2 else 0
            res = a + b + carry
            carry = res // 10
            res %= 10
            cur = ListNode(res)
            cur.next = node
            node = cur
        return node
