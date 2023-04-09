class Solution:
    def lens(self, head):
        if head is None:
            return 0
        last_node = head
        count = 0
        while last_node:
            last_node = last_node.next
            count += 1

        return count

    def middleNode(self, head):
        len_head = self.lens(head)
        index_left_ans = len_head // 2

        current_head = head
        for i in range(index_left_ans):
            current_head = current_head.next
        head = current_head

        return head
