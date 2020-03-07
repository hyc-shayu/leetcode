from src.tool.struct import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        my_head = ListNode(0)
        my_head.next = head
        next_node = my_head
        tmp_list = []
        while next_node:
            tmp_list.append(next_node)
            if len(tmp_list) > n + 1:
                tmp_list.pop(0)
            next_node = next_node.next

        tmp_list[0].next = tmp_list[1].next
        return my_head.next

    def removeNthFromEnd1(self, head: ListNode, n: int) -> ListNode:
        my_head = ListNode(0)
        my_head.next = head
        next_node = my_head
        # 使用指针加固定长度数组 模拟队列
        queue_len = n + 1
        tmp_list = [None] * queue_len
        cur = 0
        while next_node:
            tmp_list[cur % queue_len] = next_node
            next_node = next_node.next
            cur += 1

        tmp_list[cur % queue_len].next = tmp_list[(cur + 1) % queue_len].next
        return my_head.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    print(node1)
    s = Solution()
    res = s.removeNthFromEnd1(node1, 2)
    print(res)
