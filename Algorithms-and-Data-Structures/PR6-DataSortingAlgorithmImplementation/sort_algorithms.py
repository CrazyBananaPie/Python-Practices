class MergeSort:
    def start_merge_sorting(self, array: list, attr: str):
        if len(array) in range(2):
            return array

        k = 1
        while k < len(array):
            for i in range(0, len(array) - k, 2 * k):
                array[i:i + 2 * k] = self.__merging_process(array[i:i + k], array[i + k:i + 2 * k], attr)
            k *= 2

    @staticmethod
    def __merging_process(array1: list, array2: list, attr: str) -> list:
        array_output = []
        i = j = 0
        while i < len(array1) and j < len(array2):
            a1 = getattr(array1[i], attr)
            a2 = getattr(array2[j], attr)
            if a1 < a2:
                array_output.append(array1[i])
                i += 1
            else:
                array_output.append(array2[j])
                j += 1

        while j < len(array2):
            array_output.append(array2[j])
            j += 1
        while i < len(array1):
            array_output.append(array1[i])
            i += 1

        return array_output


class QuickSort:
    def start_quick_sorting(self, array: list, lw: int, h: int):
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

            p = self.__partition(array, lw, h)

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

    @staticmethod
    def __partition(array: list, lw: int, h: int):
        i = (lw - 1)
        x = array[h]

        for j in range(lw, h):
            if array[j] <= x:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[h] = array[h], array[i + 1]
        return i + 1


class SortAlgorithms(QuickSort, MergeSort):
    def __init__(self):
        super().__init__()

    def sort(self, array: list) -> bool:
        super().start_quick_sorting(array, 0, array.__len__() - 1)
        return True

    def sort_by(self, array: list, attr: str) -> bool:
        try:
            getattr(array[0], attr)
        except AttributeError:
            return False

        super().start_merge_sorting(array, attr)
        return True
