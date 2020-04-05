from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 0
        self.pre = None
        self.next = None

    def insert(self, node):
        node.next = self.next
        node.pre = self
        self.next.pre = node
        self.next = node


def create_link():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.next = tail
    tail.pre = head
    return head, tail


class LFUCache:
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._size = 0
        self._key_map = {}
        self._freq_map = defaultdict(create_link)
        self._min_freq = 0

    def _delete(self, node):
        if node.pre:
            node.pre.next = node.next
            node.next.pre = node.pre
            head, tail = self._freq_map[node.freq]
            if node.pre is head and node.next is tail:
                self._freq_map.pop(node.freq)
        return node.key

    def _increase(self, node):
        self._delete(node)
        node.freq += 1
        head, tail = self._freq_map[node.freq]
        # 后更新排在后
        tail.pre.insert(node)
        if node.freq == 1:
            self._min_freq = 1
        elif self._min_freq == node.freq - 1:
            head, tail = self._freq_map[node.freq - 1]
            if head.next is tail:
                self._min_freq = node.freq

    def get(self, key: int) -> int:
        res = self._key_map.get(key, -1)
        if res == -1:
            return res
        self._increase(res)
        return res.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        if key in self._key_map:
            node = self._key_map[key]
            node.val = value
        else:
            node = Node(key, value)
            self._key_map[key] = node
            self._size += 1
        if self._size > self._capacity:
            self._size -= 1
            deleted = self._delete(self._freq_map[self._min_freq][0].next)
            self._key_map.pop(deleted)
        self._increase(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    inp1 = ["LFUCache", "put", "put", "put", "put", "get", "get"]
    inp2 = [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]]
    cache = eval(f'{inp1[0]}({inp2[0][0]})')
    for i in range(1, len(inp1)):
        print(eval(f'cache.{inp1[i]}{tuple(inp2[i])}'))
