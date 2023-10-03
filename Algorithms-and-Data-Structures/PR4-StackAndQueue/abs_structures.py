from abc import ABC, abstractmethod


class AbsStack(ABC):

    @abstractmethod
    def push(self, value: object) -> bool:
        ...

    @abstractmethod
    def pop(self) -> object:
        ...

    @abstractmethod
    def top(self) -> object:
        ...


class AbsQueue(ABC):

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
