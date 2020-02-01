from src.tool.struct import ListNode
import random

__defaultLen = 5
__minVal = 1
__maxVal = 10


def getNodeList(length=__defaultLen, minVal=__minVal, maxVal=__maxVal):
    head = ListNode(-1)
    cur = head
    for i in range(length):
        cur.next = ListNode(random.randint(minVal, maxVal))
        cur = cur.next
    return head.next


def getSortedNodeList(length=__defaultLen, minVal=__minVal, maxVal=__maxVal):
    sortedList = [random.randint(minVal, maxVal) for _ in range(length)]
    sortedList.sort()
    head = ListNode(-1)
    cur = head
    for v in sortedList:
        cur.next = ListNode(v)
        cur = cur.next
    return head.next

