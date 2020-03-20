from typing import List


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:

        if not arr or k < 1:
            return []

        # MAX_INT = 1<<31 - 1
        # heap = [MAX_INT] * k
        heap = arr[:k]

        def insert_max_heap(number):
            if number >= heap[0]:
                return
            heap[0] = number
            heapfy(0)

        def init_max_heap():
            for i in reversed(range(k // 2)):
                heapfy(i)

        def heapfy(idx):
            left = idx * 2 + 1
            if left >= k:
                return
            right = left + 1
            max_idx = idx
            if heap[left] > heap[max_idx]:
                max_idx = left
            if right < k and heap[right] > heap[max_idx]:
                max_idx = right
            if max_idx == idx:
                return
            heap[idx], heap[max_idx] = heap[max_idx], heap[idx]

            heapfy(max_idx)

        init_max_heap()

        for digit in arr[k:]:
            insert_max_heap(digit)
        return heap


if __name__ == '__main__':
    print(Solution().getLeastNumbers([0, 0, 1, 2, 4, 2, 2, 3, 1, 4], 8))
