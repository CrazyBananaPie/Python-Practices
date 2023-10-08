from typing import Optional

from models_and_generators import RAM


class FibonacciAlgorithm:
    @staticmethod
    def start_fib_alg(body, val) -> int | None:
        fib_num_1 = 0
        fib_num_2 = 1
        fib_sum = fib_num_2 + fib_num_1
        while fib_sum < len(body):
            fib_num_1 = fib_num_2
            fib_num_2 = fib_sum
            fib_sum = fib_num_2 + fib_num_1

        index = -1
        while fib_sum > 1:
            i = min(index + fib_num_1, (len(body) - 1))
            if body[i] < val:
                fib_sum = fib_num_2
                fib_num_2 = fib_num_1
                fib_num_1 = fib_sum - fib_num_2
                index = i
            elif body[i] > val:
                fib_sum = fib_num_1
                fib_num_2 = fib_num_2 - fib_num_1
                fib_num_1 = fib_sum - fib_num_2
            else:
                return i
        if fib_num_2 and index < (len(body) - 1) and body[index + 1] == val:
            return index + 1
        return None


class ExponentialAlgorithm:
    def __init__(self):
        self.__body_used: list = [None]
        self.__value: Optional[list] = None
        self.__template: dict = {}

    def start_exp_alg(self, body: list, attrs: list, vals: list) -> int | None:
        self.__template = dict(zip(attrs, vals))
        self.__value = list(self.__template.values())
        self.__body_used = body

        if not self.__check_attr(self.__template):
            print("ATTRIBUTE ERROR")
            return None

        attribute_list = []
        for attr in self.__template.keys():
            attribute_list.append(getattr(self.__body_used[0], attr))

        if self.__value == attribute_list:
            return 0

        pos = 1
        while pos < len(body) and attribute_list <= self.__value:
            attribute_list = []
            for attr in self.__template.keys():
                attribute_list.append(getattr(self.__body_used[pos], attr))
            pos *= 2

        self.__body_used = body[:pos]
        return self.__binary_search(0, len(self.__body_used) - 1)

    def __check_attr(self, template: dict) -> bool:
        if len(template) not in range(1, 7):
            return False
        for attr in template.keys():
            try:
                getattr(self.__body_used[0], attr)
            except AttributeError:
                return False
        return True

    def __binary_search(self, left: int, right: int) -> int | None:
        middle = (left + right) // 2

        arr_list = []
        for attr in self.__template.keys():
            arr_list.append(getattr(self.__body_used[middle], attr))

        if self.__value == arr_list:
            return middle
        elif left > right:
            return None
        elif self.__value > arr_list:
            return self.__binary_search(middle + 1, right)
        elif self.__value < arr_list:
            return self.__binary_search(left, middle - 1)


class SearchAlgorithms(FibonacciAlgorithm, ExponentialAlgorithm):
    def __init__(self):
        super().__init__()

    def find_object(self, body: list, value: RAM) -> int | None:
        return super().start_fib_alg(body, value)

    def find_object_by_attributes(self, body: list, attrs: list, vals: list) -> int | None:
        return super().start_exp_alg(body, attrs, vals)
