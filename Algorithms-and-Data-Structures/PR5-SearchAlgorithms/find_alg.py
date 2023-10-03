from pr_2 import RAM
from org_array import OrganizedArr


class FibSearch:
    def fib_alg(self, body, val) -> [int, None]:
        fib_2 = 0
        fib_1 = 1
        fib_s = fib_1 + fib_2
        while fib_s < len(body):
            fib_2 = fib_1
            fib_1 = fib_s
            fib_s = fib_1 + fib_2
        index = -1
        while fib_s > 1:
            i = min(index + fib_2, (len(body) - 1))
            if body[i] < val:
                fib_s = fib_1
                fib_1 = fib_2
                fib_2 = fib_s - fib_1
                index = i
            elif body[i] > val:
                fib_s = fib_2
                fib_1 = fib_1 - fib_2
                fib_2 = fib_s - fib_1
            else:
                return i
        if fib_1 and index < (len(body) - 1) and body[index + 1] == val:
            return index + 1
        return None


class ExponentialSearch:
    def __init__(self):
        self.__body_used: list = [None]
        self.__value: [None, list] = None
        self.__template: dict = {}

    def exp_alg(self, body: list, attrs: list, vars: list) -> [None, int]:
        self.__template = dict(zip(attrs, vars))
        self.__value = list(self.__template.values())
        self.__body_used = body

        if not self.__check_attr(self.__template):
            print("ATTRIBUTE ERROR")
            return None

        arr_list = []
        for attr in self.__template.keys():
            arr_list.append(getattr(self.__body_used[0], attr))

        if self.__value == arr_list:
            return 0

        pos = 1
        while pos < len(body) and arr_list <= self.__value:
            arr_list = []
            for attr in self.__template.keys():
                arr_list.append(getattr(self.__body_used[pos], attr))
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

    def __binary_search(self, left: int, right: int) -> [None, int]:
        mid = (left + right) // 2

        arr_list = []
        for attr in self.__template.keys():
            arr_list.append(getattr(self.__body_used[mid], attr))

        if self.__value == arr_list:
            return mid
        elif left > right:
            return None
        elif self.__value > arr_list:
            return self.__binary_search(mid + 1, right)
        elif self.__value < arr_list:
            return self.__binary_search(left, mid - 1)


class FindAlg(OrganizedArr, FibSearch, ExponentialSearch):
    def __init__(self):
        super().__init__()

    def obj_find(self, value: RAM) -> [None, int]:
        return super().fib_alg(self.get_all(), value)

    def find_by_attr(self, attrs: list, vars: list) -> [None, int]:
        return super().exp_alg(self.get_all(), attrs, vars)
