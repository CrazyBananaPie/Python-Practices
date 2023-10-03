from dyn_array import DynamicArr


class MergeSort:
    def merge_alg(self, org_array: list, attr: str) -> list:
        if len(org_array) in range(2):
            return org_array

        k = 1
        while k < len(org_array):
            for i in range(0, len(org_array) - k, 2 * k):
                org_array[i:i + 2 * k] = self.__merging_proc(org_array[i:i + k], org_array[i + k:i + 2 * k], attr)
            k *= 2

        return org_array

    @staticmethod
    def __merging_proc(array1: list, array2: list, attr: str) -> list:
        array_res = []
        i = j = 0
        while i < len(array1) and j < len(array2):
            a1 = getattr(array1[i], attr)
            a2 = getattr(array2[j], attr)
            if a1 < a2:
                array_res.append(array1[i])
                i += 1
            else:
                array_res.append(array2[j])
                j += 1

        while j < len(array2):
            array_res.append(array2[j])
            j += 1
        while i < len(array1):
            array_res.append(array1[i])
            i += 1

        return array_res


class SpeedSort:
    @staticmethod
    def partition(arr: list, lw: int, h: int):
        i = (lw - 1)
        x = arr[h]

        for j in range(lw, h):
            if arr[j] <= x:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[h] = arr[h], arr[i + 1]
        return i + 1

    def speed_alg(self, arr: list, lw: int, h: int):
        size = h - lw + 1
        stack = [0] * size

        top = -1

        top = top + 1
        stack[top] = lw
        top = top + 1
        stack[top] = h

        while top >= 0:

            h = stack[top]
            top = top - 1
            lw = stack[top]
            top = top - 1

            p = self.partition(arr, lw, h)

            if p - 1 > lw:
                top = top + 1
                stack[top] = lw
                top = top + 1
                stack[top] = p - 1

            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h


class SortAlg(DynamicArr, SpeedSort, MergeSort):
    def __init__(self):
        super().__init__()

    def sort(self) -> bool:
        new_array = self.get_all()
        super().speed_alg(new_array, 0, len(self.get_all()) - 1)
        for key, el in enumerate(new_array):
            self.array[key] = el
        return True

    def sort_by(self, attr) -> bool:
        try:
            getattr(self.get_all()[0], attr)
        except AttributeError:
            return False

        new_array = super().merge_alg(self.get_all(), attr)
        for key, el in enumerate(new_array):
            self.array[key] = el
        return True
