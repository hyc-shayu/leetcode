class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def get_list(self):
        val_list = [self.val]
        next_node = self.next
        while next_node:
            val_list.append(next_node.val)
            next_node = next_node.next
        return ' '.join(map(str, val_list))

    def __str__(self):
        return f"{self.val} -> {self.next.val if self.next else None}"
