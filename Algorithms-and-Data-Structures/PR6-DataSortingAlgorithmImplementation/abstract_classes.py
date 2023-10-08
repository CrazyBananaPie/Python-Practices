from abc import ABC, abstractmethod


class AbstractList(ABC):
    @abstractmethod
    def add(self, value: object, index: int) -> bool:
        ...

    @abstractmethod
    def insert(self, value: object, index: int) -> bool:
        ...

    @abstractmethod
    def find(self, value: object) -> int:
        ...

    @abstractmethod
    def get(self, index: int) -> object:
        ...

    @abstractmethod
    def remove(self, value: object) -> bool:
        ...

    @abstractmethod
    def get_all(self) -> list:
        ...
