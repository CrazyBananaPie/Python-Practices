from AbstractModule import ListAbsCommands
from pr_2 import RAM
from node import Node


class SingleLinkList(ListAbsCommands):

    def __init__(self):
        __node: object = Node(None)
        self.__list_start: object = __node
        self.length: int = 0

    def add(self, value: RAM, index: int = None) -> bool:
        cur_el = self.__list_start
        new_el = Node(value)

        if index is not None and index in range(self.length):
            i = 0
            while True:
                back_el = cur_el
                cur_el = cur_el.next

                if i == index:
                    back_el.next = new_el
                    new_el.next = cur_el
                    self.length += 1
                    return True

                i += 1

        elif index is None:
            while cur_el.next:
                cur_el = cur_el.next
            cur_el.next = new_el
            self.length += 1
            return True

        else:
            return False

    def insert(self, value: object, index: int) -> bool:
        cur_el = self.__list_start

        if index in range(self.length):
            i = 0
            while True:
                cur_el = cur_el.next
                if i == index:
                    cur_el.data = value
                    return True

                i += 1

        else:
            return False

    def remove(self, value: object) -> bool:
        cur_el = self.__list_start

        while True:
            back_el = cur_el
            cur_el = cur_el.next

            if cur_el.data == value:
                back_el.next = cur_el.next
                self.length -= 1
                return True
            elif not cur_el.next and cur_el.data != value:
                return False

    def find(self, value: object) -> int:
        cur_el = self.__list_start

        i = 0
        while True:
            cur_el = cur_el.next

            if cur_el.data == value:
                return i
            elif not cur_el.next and cur_el.data != value:
                return False

            i += 1

    def get(self, index: int) -> object:
        cur_el = self.__list_start

        if isinstance(index, int) and index in range(self.length):
            i = 0
            while True:
                cur_el = cur_el.next

                if i == index:
                    return cur_el.data

                i += 1

        else:
            return None

    def get_all(self) -> list:
        cur_el = self.__list_start
        all_el = []
        while cur_el.next:
            cur_el = cur_el.next
            all_el.append(cur_el.data)

        return all_el

    def __repr__(self):
        return f'{self.get_all()}'
