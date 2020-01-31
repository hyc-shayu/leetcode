# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        _str = [self.val]
        next_node = self.next
        while next_node:
            _str.append(next_node.val)
            next_node = next_node.next
        return ' '.join(map(str, _str))


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        myHead = ListNode(0)
        myHead.next = head
        nextNode = myHead
        l = []
        while nextNode:
            l.append(nextNode)
            if len(l) > n + 1:
                l.pop(0)
            nextNode = nextNode.next

        l[0].next = l[1].next
        return myHead.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        myHead = ListNode(0)
        myHead.next = head
        nextNode = myHead
        # 使用指针加固定长度数组 模拟队列
        queueLen = n + 1
        l = [None] * queueLen
        cur = 0
        while nextNode:
            l[cur % queueLen] = nextNode
            nextNode = nextNode.next
            cur += 1

        l[cur % queueLen].next = l[(cur + 1) % queueLen].next
        return myHead.next


if __name__ == '__main__':
    head = ListNode(1)
    head1 = ListNode(2)
    head.next = head1
    print(head)
    s = Solution()
    res = s.removeNthFromEnd1(head, 2)
    print(res)
