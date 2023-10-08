from abc import ABC, abstractmethod


class AbstractStack(ABC):

    @abstractmethod
    def push(self, value: object) -> bool:
        ...

    @abstractmethod
    def pop(self) -> object:
        ...

    @abstractmethod
    def top(self) -> object:
        ...


class AbstractQueue(ABC):

    @abstractmethod
    def enqueue(self, value: object) -> bool:
        ...

    @abstractmethod
    def dequeue(self) -> object:
        ...

    @abstractmethod
    def get_all(self) -> list:
        ...

    @abstractmethod
    def front(self) -> object:
        ...

    @abstractmethod
    def __len__(self) -> int:
        ...
