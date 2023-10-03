from abs_structures import AbsStack
from nodes import Node
from cls_gen_and_ram import RAM


class Stack(AbsStack):

    def __init__(self):
        node = Node(None)
        self.__head = node
        self.__cur_top = self.__head

    def push(self, value: RAM) -> bool:
        head = self.__head
        old_top = self.__head.next
        new_top = Node(value)

        head.next = new_top
        new_top.next = old_top
        self.__cur_top = new_top
        return True

    def pop(self) -> [RAM, None]:

        if self.__head.next:
            head = self.__head
            remove_top = head.next
            new_top = remove_top.next

            head.next = new_top
            self.__cur_top = new_top

            return remove_top.data

        else:
            return None

    def top(self) -> [RAM, None]:
        if self.__cur_top:
            return self.__cur_top.data
        else:
            return None
