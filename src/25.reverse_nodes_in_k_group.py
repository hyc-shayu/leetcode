from src.tool.struct import ListNode
from src.tool.test_data import get_sorted_node_list


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        my_head = ListNode(-1)
        my_head.next = head

        pre_head = my_head
        end = head

        while end:
            # 获取结束节点
            count = 1
            while count < k and end:
                count += 1
                end = end.next

            # 如果节点长度不够 就可以结束了
            if count < k or not end:
                break

            start = pre_head.next  # head -> 1
            stop = end.next  # k+1的节点
            pre_head.next = end  # head -> end
            pre = start
            tmp_node = start.next

            # 第二个节点开始 指向 前一个节点
            while tmp_node is not stop:
                tmp_next = tmp_node.next  # 记录下一个节点
                tmp_node.next = pre  # 指向前一个节点
                pre = tmp_node  # 记录当前节点
                tmp_node = tmp_next  # 下一个节点

            # 交换首尾连接处
            start.next = stop
            pre_head = start
            end = stop

        return my_head.next


if __name__ == '__main__':
    node = get_sorted_node_list()
    print(node.get_list())
    print((Solution().reverseKGroup(node, 2)).get_list())
