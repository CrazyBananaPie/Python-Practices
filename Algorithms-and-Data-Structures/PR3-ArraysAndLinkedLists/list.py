from AbstractModule import ListAbsCommands
from pr_2 import RAM


class JustList(ListAbsCommands):
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

    def get(self, index: int) -> [RAM, None]:
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