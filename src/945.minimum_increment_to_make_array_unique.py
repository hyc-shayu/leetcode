from typing import List
from queue import PriorityQueue


class Solution:
    def minIncrementForUnique(self, list_: List[int]) -> int:
        if not list_:
            return 0

        pq = PriorityQueue()
        for digit in list_:
            pq.put(digit)
        min_ = pq.get()
        count = 0
        while not pq.empty():
            top = pq.get()
            if top > min_:
                min_ = top
                continue
            count += min_ - top + 1
            min_ += 1
        return count
