from src.tool.struct import ListNode, TreeNode
import random

_defaultLen = 5
_min_val = 1
_max_val = 10


def get_node_list(list_):
    head = ListNode(-1)
    cur = head
    for item in list_:
        cur.next = ListNode(item)
        cur = cur.next
    return head.next


def get_rand_node_list(length=_defaultLen, min_val=_min_val, max_val=_max_val):
    head = ListNode(-1)
    cur = head
    for i in range(length):
        cur.next = ListNode(random.randint(min_val, max_val))
        cur = cur.next
    return head.next


def get_sorted_node_list(length=_defaultLen, min_val=_min_val, max_val=_max_val):
    sorted_list = [random.randint(min_val, max_val) for _ in range(length)]
    sorted_list.sort()
    head = ListNode(-1)
    cur = head
    for v in sorted_list:
        cur.next = ListNode(v)
        cur = cur.next
    return head.next


def string_to_tree_node(input_):
    input_ = input_.strip()
    input_ = input_[1:-1]
    if not input_:
        return None

    input_values = [s.strip() for s in input_.split(',')]
    root = TreeNode(int(input_values[0]))
    node_queue = [root]
    front = 0
    index = 1
    while index < len(input_values):
        node = node_queue[front]
        front = front + 1

        item = input_values[index]
        index = index + 1
        if item != "null":
            left_number = int(item)
            node.left = TreeNode(left_number)
            node_queue.append(node.left)

        if index >= len(input_values):
            break

        item = input_values[index]
        index = index + 1
        if item != "null":
            right_number = int(item)
            node.right = TreeNode(right_number)
            node_queue.append(node.right)
    return root
