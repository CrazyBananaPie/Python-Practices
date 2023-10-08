import math

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

    def sort(self) -> bool:
        self.__body.sort()
        return True

    def get_all(self) -> list:
        return self.__body

    def __repr__(self):
        return f'{self.get_all()}'


class DynamicArray:
    def __init__(self):
        self.__body: list = [None]
        self.__memory_size: int = 1
        self.length: int = 0

    def add(self, value: RAM) -> bool:
        self.__memory_control()
        self.__body[self.length] = value
        self.length += 1
        return True

    def remove(self, value: RAM) -> bool:
        if value not in self.__body[:self.length]:
            return False

        pos = 0
        deletion = False
        while self.__body[pos] is not None:
            if value == self.__body[pos]:
                deletion = True

            if deletion is True:
                self.__body[pos] = self.__body[pos + 1]
            pos += 1

        self.length -= 1
        self.__memory_control()
        return True

    def __memory_control(self):
        if self.__memory_size == self.length:
            self.__memory_size *= 2
            buffer_body = [None] * self.__memory_size
            for key, el in enumerate(self.__body):
                buffer_body[key] = el
            self.__body = buffer_body

        elif self.length < self.__memory_size / 2:
            self.__memory_size = math.ceil(self.__memory_size / 2)
            buffer_body = [None] * self.__memory_size
            for key, el in enumerate(self.__body[:self.length]):
                buffer_body[key] = el
            self.__body = buffer_body

    def get(self, index: int) -> [RAM, None]:
        if index not in range(self.length):
            return None

        return self.__body[index]

    def find(self, value: RAM) -> [int, None]:
        if value not in self.__body[:self.length]:
            return None

        pos = 0
        while self.__body[pos] is not None:
            if value == self.__body[pos]:
                return pos
            pos += 1

    def get_all(self) -> list:
        return self.__body[:self.length]

    @property
    def array(self):
        return self.__body

    def __repr__(self) -> str:
        return f'{self.__body[:self.length]}'

    def __len__(self) -> int:
        return self.length
