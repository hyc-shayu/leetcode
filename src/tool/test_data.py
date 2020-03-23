from src.tool.struct import ListNode
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
