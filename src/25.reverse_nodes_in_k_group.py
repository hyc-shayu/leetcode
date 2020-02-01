from src.tool.struct import ListNode
from src.tool.test_data import getSortedNodeList


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        myHead = ListNode(-1)
        myHead.next = head

        preHead = myHead
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

            start = preHead.next  # head -> 1
            stop = end.next  # k+1的节点
            preHead.next = end  # head -> end
            pre = start
            tmpNode = start.next

            # 第二个节点开始 指向 前一个节点
            while tmpNode is not stop:
                tmpNext = tmpNode.next  # 记录下一个节点
                tmpNode.next = pre  # 指向前一个节点
                pre = tmpNode  # 记录当前节点
                tmpNode = tmpNext  # 下一个节点

            # 交换首尾连接处
            start.next = stop
            preHead = start
            end = stop

        return myHead.next


if __name__ == '__main__':
    node = getSortedNodeList()
    print(node.get_list())
    print((Solution().reverseKGroup(node, 2)).get_list())
