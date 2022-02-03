from typing import Any


class Node:

    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return f"Node {self.value}"


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.lenght = 0

    def __str__(self) -> str:
        if self.head is not None:
            current = self.head
            values = [str(current.value)]
            while current.next is not None:
                current = current.next
                values.append(str(current.value))
            return "[{values}]".format(values=" ".join(values))
        return "LinkedList []"

    def append(self, val: Any) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        self.lenght += 1

    def remove(self, index: int):
        cur_node = self.head
        cur_index = 0
        if self.lenght == 0 or self.lenght <= index:
            raise IndexError
        if cur_node is not None:
            if index == 0:
                self.head = cur_node.next
                self.lenght -= 1
                return

        while cur_node is not None:
            if cur_index == index:
                break
            prev = cur_node
            cur_node = cur_node.next
            cur_index += 1
        prev.next = cur_node.next
        self.lenght -= 1
