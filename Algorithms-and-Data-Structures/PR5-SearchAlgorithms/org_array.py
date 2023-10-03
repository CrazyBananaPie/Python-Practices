import math
from pr_2 import RAM


class OrganizedArr:
    def __init__(self):
        self.__body: list = [None]
        self.__memory_size: int = 1
        self.length: int = 0

    def add(self, value: RAM) -> bool:
        self.__memory_control()

        pos = 0
        while self.__body[pos] is not None:
            if self.__body[pos] >= value:
                i = self.length
                while i > pos:
                    self.__body[i] = self.__body[i - 1]
                    i -= 1
                self.__body[pos] = value
                self.length += 1
                return True
            pos += 1

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
