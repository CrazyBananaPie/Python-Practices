from abs_structures import AbsQueue
from nodes import Node, Node2Link
from cls_gen_and_ram import RAM


class QueueL(AbsQueue):

    def __init__(self):
        node = Node(None)
        self.__head = node
        self.__front = None
        self.__length = 0

    def enqueue(self, value: RAM) -> bool:
        head = self.__head
        old_elem = head.next
        new_elem = Node2Link(value)

        head.next = new_elem
        new_elem.next = old_elem

        if old_elem is None:
            self.__front = new_elem
        else:
            old_elem.prev = new_elem

        self.__length += 1
        return True

    def dequeue(self) -> [RAM, None]:
        front = self.__front

        if front == self.__head:
            return None

        if front and front.prev:
            new_front = front.prev
            new_front.next = None
            self.__front = new_front

            self.__length -= 1
            return front.data

        elif front and front.prev is None:
            self.__head.next = None
            self.__front = self.__head

            self.__length -= 1
            return front.data

    def front(self) -> [RAM, None]:
        if self.__front:
            return self.__front.data
        else:
            return None

    def get_all(self) -> list:
        head = self.__head
        cur_el = head
        elements = []

        while cur_el.next:
            cur_el = cur_el.next
            elements.append(cur_el.data)

        return elements

    def __len__(self) -> int:
        return self.__length
