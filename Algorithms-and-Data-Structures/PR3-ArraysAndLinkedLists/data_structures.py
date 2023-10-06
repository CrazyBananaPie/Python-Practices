from typing import Optional

from abstract_classes import AbstractList
from models_and_generators import RAM

class SimpleList(AbstractList):
    def __init__(self):
        self.__body: list = []
        self.size: int = 0

    def add(self, value: RAM, index: int = None) -> bool:
        if index is None:
            self.__body.append(value)
            self.size += 1
            return True
        elif index not in range(self.size):
            return False
        else:
            self.__body.insert(index, value)
            self.size += 1
            return True

    def insert(self, value: RAM, index: int) -> bool:
        if index not in range(self.size):
            return False
        else:
            self.__body[index] = value
            return True

    def find(self, value: RAM) -> int:
        if value not in self.__body:
            return False
        else:
            return self.__body.index(value)

    def get(self, index: int) -> RAM | None:
        if index not in range(self.size):
            return None
        else:
            return self.__body[index]

    def remove(self, value: RAM) -> bool:
        if self.size == 0 or value not in self.__body:
            return False
        else:
            self.__body.remove(value)
            self.size -= 1
            return True

    def get_all(self) -> list:
        return self.__body

    def __repr__(self):
        return f'{self.get_all()}'


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next: Optional[ListNode] = None


class SingleLinkedList(AbstractList):
    def __init__(self):
        __node: object = ListNode(None)
        self.__list_start: object = __node
        self.length: int = 0

    def add(self, value: RAM, index: int = None) -> bool:
        current_node = self.__list_start
        new_node = ListNode(value)

        if index is not None and index in range(self.length):
            i = 0
            while True:
                previous_node = current_node
                current_node = current_node.next

                if i == index:
                    previous_node.next = new_node
                    new_node.next = current_node
                    self.length += 1
                    return True

                i += 1

        elif index is None:
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
            self.length += 1
            return True

        else:
            return False

    def insert(self, value: object, index: int) -> bool:
        current_node = self.__list_start

        if index in range(self.length):
            i = 0
            while True:
                current_node = current_node.next
                if i == index:
                    current_node.data = value
                    return True

                i += 1

        else:
            return False

    def remove(self, value: object) -> bool:
        current_node = self.__list_start

        while True:
            previous_node = current_node
            current_node = current_node.next

            if current_node.data == value:
                previous_node.next = current_node.next
                self.length -= 1
                return True
            elif not current_node.next and current_node.data != value:
                return False

    def find(self, value: object) -> int | bool:
        current_node = self.__list_start

        i = 0
        while True:
            current_node = current_node.next

            if current_node.data == value:
                return i
            elif not current_node.next and current_node.data != value:
                return False

            i += 1

    def get(self, index: int) -> object | None:
        current_node = self.__list_start

        if isinstance(index, int) and index in range(self.length):
            i = 0
            while True:
                current_node = current_node.next

                if i == index:
                    return current_node.data

                i += 1

        else:
            return None

    def get_all(self) -> list:
        current_node = self.__list_start
        all_data = []
        while current_node.next:
            current_node = current_node.next
            all_data.append(current_node.data)

        return all_data

    def __repr__(self):
        return f'{self.get_all()}'