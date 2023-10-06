from typing import Optional

from abstract_classes import AbstractQueue, AbstractStack
from models_and_generators import RAM


class SingleLinkNode:
    def __init__(self, data):
        self.data = data
        self.next: Optional[DoubleLinkNode] = None


class DoubleLinkNode:
    def __init__(self, data):
        self.data = data
        self.next: Optional[DoubleLinkNode] = None
        self.previous: Optional[DoubleLinkNode] = None


class Queue(AbstractQueue):
    def __init__(self):
        node = SingleLinkNode(None)
        self.__head = node
        self.__front = None
        self.__length = 0

    def enqueue(self, value: RAM) -> bool:
        head = self.__head
        old_node = head.next
        new_node = DoubleLinkNode(value)

        head.next = new_node
        new_node.next = old_node

        if old_node is None:
            self.__front = new_node
        else:
            old_node.previous = new_node

        self.__length += 1
        return True

    def dequeue(self) -> RAM | None:
        front = self.__front

        if front == self.__head:
            return None

        if front and front.previous:
            new_front = front.previous
            new_front.next = None
            self.__front = new_front

            self.__length -= 1
            return front.data

        elif front and front.previous is None:
            self.__head.next = None
            self.__front = self.__head

            self.__length -= 1
            return front.data

    def front(self) -> RAM | None:
        if self.__front:
            return self.__front.data
        else:
            return None

    def get_all(self) -> list:
        current_node = self.__head
        all_data = []

        while current_node.next:
            current_node = current_node.next
            all_data.append(current_node.data)

        return all_data

    def __len__(self) -> int:
        return self.__length


class Stack(AbstractStack):
    def __init__(self):
        node = SingleLinkNode(None)
        self.__head = node
        self.__current_top = self.__head

    def push(self, value: RAM) -> bool:
        head = self.__head
        old_top_node = self.__head.next
        new_top_node = SingleLinkNode(value)

        head.next = new_top_node
        new_top_node.next = old_top_node
        self.__current_top = new_top_node
        return True

    def pop(self) -> RAM | None:
        if self.__head.next:
            head = self.__head
            top_node_to_remove = head.next
            new_top_node = top_node_to_remove.next

            head.next = new_top_node
            self.__current_top = new_top_node

            return top_node_to_remove.data

        else:
            return None

    def top(self) -> RAM | None:
        if self.__current_top:
            return self.__current_top.data
        else:
            return None
