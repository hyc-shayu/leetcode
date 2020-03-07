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

    # 两两合并
    def mergeKLists(self, lists):
        if not lists:
            return None

        length = len(lists)
        while length > 1:
            for i in range(length // 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[length - i - 1])
            length = (length + 1) // 2
        return lists[0]

    # 最小堆 法
    def mergeKLists1(self, lists):
        if not lists:
            return None

        arr = []
        for kList in lists:
            if kList:
                arr.append(kList)

        length = len(arr)
        if length == 0:
            return None

        solution_min_heapify(arr)
        head = cur = arr[0]

        while length > 1:
            if arr[0].next:
                arr[0] = arr[0].next
            else:
                arr[0] = arr.pop()
                length -= 1
            solution_min_heapify_1(arr, length, 0)
            cur.next = arr[0]
            cur = arr[0]

        return head


def solution_min_heapify(arr):
    length = len(arr)
    for i in reversed(range(length // 2)):
        solution_min_heapify_1(arr, length, i)


def solution_min_heapify_1(arr, length, top_index):
    left_son = 2 * top_index + 1
    right_son = 2 * top_index + 2

    while left_son < length:
        min_son = left_son
        if right_son < length and arr[right_son].val < arr[left_son].val:
            min_son = right_son
        if arr[min_son].val >= arr[top_index].val:
            break
        arr[min_son], arr[top_index] = arr[top_index], arr[min_son]
        top_index = min_son
        left_son = top_index * 2 + 1
        right_son = top_index * 2 + 2


def heapify(arr):
    length = len(arr)
    for i in reversed(range(length // 2)):
        heapify_1(arr, length, i)


def heapify_1(arr, length, i):
    smallest = i
    left_son = 2 * smallest + 1
    right_son = 2 * smallest + 2
    # 当交换的节点有叶子节 子树堆化被打破 需要再堆化
    while left_son < length:
        smaller_son = left_son
        if right_son < length and arr[left_son] < arr[right_son]:
            smaller_son = right_son

        if arr[smaller_son] > arr[smallest]:
            arr[smaller_son], arr[smallest] = arr[smallest], arr[smaller_son]
            smallest = smaller_son
        else:
            break

        left_son = 2 * smallest + 1
        right_son = 2 * smallest + 2


def heap_sort(arr):
    heapify(arr)
    length = len(arr)
    for i in range(length - 1):
        arr[length - i - 1], arr[0] = arr[0], arr[length - i - 1]
        heapify_1(arr, length - i - 1, 0)


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(5)
    node1.next = node2
    node2.next = node3
    arr0 = [node1]

    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3
    arr0.append(node1)

    node1 = ListNode(2)
    node2 = ListNode(6)
    node1.next = node2
    arr0.append(node1)

    head1 = Solution().mergeKLists(arr0)

    print(head1)
