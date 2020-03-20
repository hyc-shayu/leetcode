from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        if not arr or k < 1:
            return []

        heap = arr[:k]

        def insert_max_heap(number):
            if number >= heap[0]:
                return
            heap[0] = number
            heapify(0)

        def init_max_heap():
            for i in reversed(range(k // 2)):
                heapify(i)

        def heapify(root):
            while root < k // 2:
                left = root * 2 + 1
                right = left + 1
                if right < k and heap[right] > heap[left]:
                    greater_son = right
                else:
                    greater_son = left
                if heap[greater_son] < heap[root]:
                    break
                heap[root], heap[greater_son] = heap[greater_son], heap[root]
                root = greater_son

        init_max_heap()

        for digit in arr[k:]:
            insert_max_heap(digit)
        return heap


if __name__ == '__main__':
    print(Solution().getLeastNumbers([0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 8))
